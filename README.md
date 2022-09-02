# 200ok_backend
![imges](https://user-images.githubusercontent.com/104487608/185346903-65a8745b-da0f-4fb9-8d4f-a9603735332b.png)
# 녹턴앨리 B-street 지하2층 불법 입학 센터 (200ok)
해리포터 컨셉, 사람 사진을 초상화처럼 스타일을 변경하고 움직임을 추가해서 움직이는 초상화를 만들고 머신러닝을 통해 기숙사를 분류해주는 웹사이트
***
<br><br/>


## 1. 개발 기간, 참여 인원
* 개발기간: 2022.06.28 - 2022.07.05
* **Team** <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
김동근 <a href="https://github.com/yinmsk"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
노을 <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이정아 <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이현경 <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/108">블로그로 이동(☞ﾟヮﾟ)☞</a>
***
<br><br/>


## 2. 사용 기술
* Python 3.7
* Django REST Framework 3.13
 
<br><br/>


## 3. API 명세서
<a href="https://typingmylife.notion.site/MakeMigrations-API-53526cc465344be98ab4e786e487414f">API 명세서 자료</a>
<br><br/>


## 4. ERD 설계
![200ok](https://user-images.githubusercontent.com/104487608/186652733-dd0af8a2-605f-446f-b993-51fb96388c0a.png)
<br><br/>


## 5. 기능 소개
<details>
  <summary>simplejwt 를 이용한 회원 가입 기능 <a href="https://ddongkim.tistory.com/73">📄코드를 정리한 글</a></summary>
  <div markdown="1">
 
* settings.py 의 INSTALLED_APPS 에서 rest_framework_simplejwt 를 추가해 주었다.
* REST_FRAMEWORK 의 DEFAULT_AUTHENTICATION_CLASSES 에 JWTAuthentication 을 추가해 주었다.
* SIMPLE_JWT 를 추가해 토큰의 유효 시간을 설정해 주었다.
  </div>
</details>

<details>
  <summary>기숙사 테스트 문제 조회 <a href="https://github.com/zeonga1102/200ok_backend/blob/master/dormitory/views.py#L21">📄코드</a></summary>
  <div markdown="1">
 
![기숙사 문제](https://user-images.githubusercontent.com/104487608/188050990-005d0b6f-75bb-4353-9216-7b72a4ca66c8.png)
* 기숙사 배정을 위한 테스트 문제들을 조회합니다.
  </div>
</details>

<details>
  <summary>게시판 기능 <a href="https://github.com/cmjcum/200ok_backend/blob/c0a96c816e61f9f074ac612a522d1fa9775928cf/lounge/views.py#L13">📄코드</a></summary>
  <div markdown="1">
 
![image](https://user-images.githubusercontent.com/104487608/188051246-aea8f15d-9d1f-4c04-9a27-abe421cfadbc.png)
*  시리얼라이저를 통해 라운지 페이지 띄우기, 게시글 작성 및 삭제 기능을 사용합니다.
  </div>
</details>
<br><br/>


## 6. 트러블 슈팅
<details>
  <summary>cors 에러</summary>
  <div markdown="1">
 
* 프론트의 주소와 백엔드의 주소가 달라 cors 에러가 발생했다
* 공식 문서를 참조해서 해결 할 수 있었는데 문서 설명에 따라 settings.py 의 INSTALLED_APPS, MIDDLEWARE,  CORS_ALLOWED_ORGINS 설정을 통해 해결 할 수 있었다.
* INSTALLED_APPS 에 cors-headers 를 추가하였다.
* MIDDLEWARE 에 CorsMiddleware 를 추가하였다.
* CORS_ALLOWED_ORGINS 를 추가해서, 포트를 열어주었다.
  </div>
</details>
<br><br/>


## 7. 회고 느낀점
* 이번 이전에도 로그인 회원가입 기능을 했었는데 simplejwt 를 사용한 로그인 회원가입 기능은 처음이라 새로운걸 경험 할 수 있었습니다.
* cors에 에러에 관해 생각해 볼 수 없었는데 cors 에러를 해결하는 방법을 알게된 점이 인상적이었습니다.
* drf와 시리얼라이저를 처음 사용하게 되었던 프로젝트였는데 첫 사용이라 많이 어려운 프로젝트였지만 기초적인 사용법을 익힐 수 있어서 좋았습니다.
* 새로운 경험을 많이 할 수 있었던 프로젝트여서 좋았고 drf 와 시리얼라이저 사용법을 더 많이 익혀야 겠다고 느끼게 되는 프로젝트였습니다.
