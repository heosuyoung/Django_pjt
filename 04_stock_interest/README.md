# 🧠 주식 댓글 분석기

토스 증권 커뮤니티에서 특정 기업의 댓글을 수집하고,  
GPT 모델로 분석해 투자자들의 여론을 시각화하는 주식 분석 웹서비스입니다.

<br>

## 🖼 주요 기능

| 기능                           | 설명                                       |
| ------------------------------ | ------------------------------------------ |
| 🔐 회원가입 / 로그인 / 로그아웃 | Django 기본 유저 시스템 활용               |
| 📝 종목명 검색                  | 사용자 입력을 기반으로 TossInvest 크롤링   |
| 💬 댓글 수집 및 필터링          | Selenium으로 토스 증권 커뮤니티 댓글 수집  |
| 🤖 GPT 분석                     | GPT-4o-mini 모델을 통해 종합 여론 분석     |
| 📌 관심 종목 저장               | 로그인한 사용자마다 종목 저장 가능         |
| 👤 프로필 페이지                | 내 관심 종목 목록 조회 및 삭제 기능        |
| 🔄 종목 클릭 시 분석 자동 실행  | 관심 종목 클릭 시 자동 분석 결과 출력      |
| 🎨 부트스트랩 UI                | 반응형 검색창, 알림창, 로딩 스피너 등 적용 |

<br>

## 🛠 기술 스택

- **Backend**: Django 4.x, Python 3.10+
- **Frontend**: HTML, CSS (Bootstrap 5.3)
- **AI 분석**: OpenAI GPT (gpt-4o-mini)
- **크롤링**: Selenium, WebDriver Manager
- **DB**: SQLite (기본 설정)
- **기타**: CSRF 보호, 로그인 세션 처리

<br>

## 🖥 실행 방법

```bash
# 가상환경 생성 및 진입
python -m venv venv
source venv/bin/activate  # 윈도우: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 환경변수 설정
echo "OPENAI_API_KEY=sk-..." > .env

# 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 실행
python manage.py runserver
