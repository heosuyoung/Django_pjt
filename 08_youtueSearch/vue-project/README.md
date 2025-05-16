# 📺 관심 종목 영상 검색 서비스

YouTube Data API를 활용하여 관심 키워드의 영상을 검색하고,  
나중에 보고 싶은 영상과 좋아하는 채널을 저장/관리할 수 있는 Vue 기반 웹 애플리케이션입니다.

---

## 🔧 기술 스택

- **Frontend**: Vue 3 + Vite + Composition API  
- **Routing**: Vue Router  
- **상태 저장**: LocalStorage  
- **API**: YouTube Data API v3

---

## 📌 주요 기능

| 기능                     | 설명 |
|--------------------------|------|
| 🔍 관심 키워드 영상 검색  | 사용자가 입력한 검색어로 유튜브 영상 검색 |
| 🎬 영상 상세 보기        | 각 영상별 상세 페이지에서 재생 가능 |
| 💾 나중에 보기 저장     | 원하는 영상을 LocalStorage에 저장 |
| ⭐ 저장된 영상 목록 보기 | 저장한 영상들을 모아보는 전용 페이지 |
| ⭐ 좋아하는 채널 저장     | 영상 상세 페이지에서 채널 저장 및 별도 목록 확인 가능 |
| 🧭 상단 네비게이션       | 홈/검색/저장된 영상/좋아하는 채널 간 이동 지원 |

---

## 🖥️ 화면 예시

| 홈 화면 | 검색 결과 | 나중에 볼 영상 | 좋아하는 채널 |
|--------|----------|----------------|----------------|
| `🏠` 프로젝트 소개 및 진입 | `🔍` 유튜브 카드형 영상 표시 | `⭐` 저장된 영상 목록만 표시 | `⭐` 저장된 채널 목록만 표시 |

---

## 📁 프로젝트 구조

```bash
src/  
├── assets/  
├── components/  
├── router/  
│   └── index.js  
├── views/  
│   ├── HomeView.vue  
│   ├── SearchView.vue  
│   ├── DetailView.vue  
│   ├── WatchLaterView.vue  
│   └── FavoriteChannels.vue  
├── App.vue  
└── main.js  
```

## 🚀 실행 방법
``` bash
npm install
npm run dev


```
---
## 🔐 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성한 후, 아래와 같이 작성합니다:
VITE_YOUTUBE_API_KEY=발급받은_유튜브_API_키

※ 유튜브 API 키는 https://console.cloud.google.com/ 에서 발급받을 수 있습니다.

---
