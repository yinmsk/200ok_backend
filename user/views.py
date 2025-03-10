from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from multiprocessing import Process, Queue
import boto3

from user import serializers
from user.serializers import UserSerializer
from user.serializers import OriginalPicSerializer
from user.serializers import UserInfoSerializer

from deeplearning.deeplearning_make_portrait import make_portrait


class UserView(APIView):

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response({"messages" : "가입 성공"})

        else:
            return Response({"messages" : "가입 실패"})


q = Queue()
p = None
class MainView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        global q, p
        
        user_id = request.user.id
        request.data['user'] = user_id
        
        pic = request.data.pop('pic')[0]
        filename = pic.name

        s3 = boto3.client('s3')
        s3.put_object(
            ACL="public-read",
            Bucket="my-sparta",
            Body=pic,
            Key=filename,
            ContentType=pic.content_type)

        url = f'https://my-sparta.s3.ap-northeast-2.amazonaws.com/{filename}'
        request.data['pic'] = url

        original_pic_serializer = OriginalPicSerializer(data=request.data)

        if original_pic_serializer.is_valid():
            original_pic_serializer.save()

            p = Process(target=make_portrait, args=(q, url, user_id))
            p.start()

            return Response({'msg': 'send'}, status=status.HTTP_200_OK)

        return Response({"error": "failed"}, status=status.HTTP_400_BAD_REQUEST)


class InfoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        global p, q
        
        if p is not None:
            p.join()

            request.data['user'] = request.user.id
            request.data['portrait'] = q.get()

            userinfo_serializer = UserInfoSerializer(data=request.data)

            if userinfo_serializer.is_valid():
                userinfo_serializer.save()
                return Response({'msg': 'success'}, status=status.HTTP_200_OK)

        return Response({'error': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
        
