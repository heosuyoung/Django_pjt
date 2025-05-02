# 한국 은행 검색 지도 프로그램

> 전국의 은행 지점을 지역(시/군/구) 및 은행 종류별로 검색하고,  
> 출발지(멀티캠퍼스 역삼)에서 선택된 은행까지의 **자동차 경로를 지도에 표시**하는 서비스입니다.

---

## 🔍 주요 기능

- ✅ 전국 시/도/군구 행정구역 선택
- ✅ 주요 은행 18종 선택 가능
- ✅ 지도에 마커 및 은행 지점 표시
- ✅ 마커 클릭 시 출발지~도착지 간 경로 표시
- ✅ 카카오 모빌리티 길찾기 REST API 활용

---

## 🧩 기능 요약 (A~E)

### A. 카카오 지도 로드  
- JavaScript SDK 로드 및 초기 위치 설정 (역삼 멀티캠퍼스)

### B. 지역 및 은행 종류 선택  
- 시/도, 시/군/구, 은행 종류 select box 구성

### C. 검색 결과 마커 표시  
- 카카오 Places API로 은행 검색 → 지도에 마커 생성

### D. 각 지점별 검색 결과 출력  
- 선택한 조건에 맞는 지점만 마커로 표시됨

### E. 자동차 길찾기 기능  
- `/v1/directions` REST API 사용  
- vertexes를 polyline으로 지도에 선 표시  
- 경로 없을 시 안내 알림

---

## 📦 사용 방법

### 1. `apikey.js` 설정

아래 명령어로 `apikey.template.js`를 복사해 `apikey.js`로 만들고,  
카카오 API 키를 입력하세요.

```bash
cp apikey.template.js apikey.js
```

```javascript
const KAKAO_API_KEY = "YOUR_KAKAO_JAVASCRIPT_KEY";
const KAKAO_MOBILITY_KEY = "YOUR_KAKAO_MOBILITY_REST_KEY";
```

📌 `apikey.js`는 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다.

---

### 2. `index.html`에 스크립트 포함

```html
<script src="apikey.js"></script>
<script src="data.js"></script>
<script defer src="main.js"></script>
```

---

### 3. CORS 우회 설정 (개발 환경)

아래 링크에서 "Request temporary access" 버튼 클릭:  
🔗 https://cors-anywhere.herokuapp.com/corsdemo

---

## 🗺️ 경로 시각화 예시

- 출발지: 멀티캠퍼스 역삼 (자동 표시됨)
- 도착지: 사용자가 선택한 은행 지점
- 표시: 주황색 polyline 선으로 경로 표시
- 예외: 경로가 없을 경우 알림창 안내

---

## 🧪 테스트 좌표 예시

- 서울 역삼 (출발지): `37.498095, 127.02761`
- 부산 서면 (도착 예시): `35.158697, 129.060863`

---

## 📁 .gitignore 설정

```bash
apikey.js
```

---

## 🔐 `apikey.template.js` 안내

> 이 파일은 실제 API 키를 포함하지 않는 템플릿입니다.  
> `apikey.js`로 복사해 키를 입력한 뒤 사용하며, Git에는 포함되지 않습니다.

```javascript
const KAKAO_API_KEY = "YOUR_KAKAO_JAVASCRIPT_KEY";
const KAKAO_MOBILITY_KEY = "YOUR_KAKAO_MOBILITY_REST_KEY";
```
