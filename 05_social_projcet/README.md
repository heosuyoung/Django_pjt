# 📝 05-pjt: Django 회원 + 게시판 + 소셜 로그인

## 📌 프로젝트 개요
- Django를 활용한 회원 관리 및 게시판 기능 구현
- 로그인, 회원가입, 프로필, 팔로우, 댓글 기능 구현
- Google 소셜 로그인(OAuth 2.0) 도전 과제 완료

---

## 📁 앱 구성

### 🔐 accounts 앱
- 사용자 모델 커스텀 (AbstractUser 상속)
- 회원가입 / 로그인 / 로그아웃
- 사용자 프로필 (작성 글, 댓글, 팔로워/팔로잉)
- 팔로우 / 언팔로우 기능
- Google 소셜 로그인 구현

### 📝 boards 앱
- 게시글 CRUD (글쓰기, 상세조회, 수정, 삭제)
- 댓글 기능 (작성, 삭제, 대댓글 포함)
- 본인만 수정/삭제 가능

---

## ✅ 기능 요약

| 기능 | 설명 |
|------|------|
| 회원가입 / 로그인 / 로그아웃 | Django 내장 인증 기능 활용 |
| 프로필 페이지 | 본인 글, 댓글, 팔로우 수 등 표시 |
| 팔로우 기능 | 다른 유저 팔로우/언팔로우 가능 |
| 게시판 | 글 작성, 수정, 삭제, 댓글 가능 |
| 댓글 | 대댓글 구조 구현 (`parent_comment`) |
| 소셜 로그인 | Google OAuth2.0 API 적용 |

---

## 🛠 기술 스택

- Python 3.9+
- Django 4.2+
- HTML (Django 템플릿)
- SQLite3
- GCP OAuth 2.0
- `django-environ` (환경변수 관리)

---

## 🔐 .env 예시

```env
SECRET_KEY="your-django-secret-key"
DEBUG=True
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"

##실행방법

# 프로젝트 클론
git clone [레포지토리 주소]
cd [프로젝트 폴더명]

# 가상환경 생성 및 실행
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# .env 파일 생성 (위 예시 참고)

# 마이그레이션 + 관리자 생성
python manage.py migrate
python manage.py createsuperuser

# 서버 실행
python manage.py runserver
