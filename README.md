# Oil Today® - 스마트 주유소 추천 대시보드

한남대학교 프로그램호환 프로젝트

## 🌐 프로젝트 소개

Oil Today®는 실시간 유가 정보를 제공하고 주변 주유소를 추천하는 스마트 대시보드 웹 애플리케이션입니다. 사용자의 현재 위치를 기반으로 최적의 주유소를 찾아주고, 지역별 유가 정보를 시각화하여 제공합니다.

**라이브 데모**: [https://dev.dcarecloud.com/~stud_09/program_hoho/index.html](https://dev.dcarecloud.com/~stud_09/program_hoho/index.html)

## 👥 팀원

- 노건우
- 조준하
- 김재현
- 윤홍식
- 박동균

## ✨ 주요 기능

### 1. 실시간 유가 정보 제공
- **휘발유 (Gasoline)**: 전국 시도별 휘발유 가격 정보
- **고급휘발유 (High-Octane)**: 고급 휘발유 가격 정보
- **경유 (Diesel)**: 경유 가격 정보
- **LPG (액화석유가스)**: LPG 가격 정보

### 2. 데이터 시각화
- 지역별 유가 차트 (Chart.js 활용)
- 가격 변동 추이 시각화
- 전국 평균 및 주요 지역 가격 비교

### 3. 주변 주유소 찾기
- 현재 위치 기반 주변 주유소 검색
- Google Maps / Naver Maps API 연동
- 주유소 위치 및 정보 표시
- 경로 안내 기능

### 4. 유가 관련 뉴스
- Google News RSS 피드 연동
- 실시간 유가 관련 뉴스 제공
- 5분마다 자동 업데이트

### 5. 위치 기반 서비스
- Geolocation API를 통한 현재 위치 파악
- 위치 기반 유가 정보 제공
- 주변 주유소 추천

## 🛠️ 기술 스택

### Frontend
- **HTML5** / **CSS3** / **JavaScript (ES6+)**
- **Chart.js**: 데이터 시각화
- **Google Maps API**: 지도 및 주유소 검색
- **Naver Maps API**: 지도 서비스 (경유 페이지)

### Backend
- **Python 3.x**
- **Flask**: RESTful API 서버
- **Flask-CORS**: CORS 처리

### Data
- **OPINET API**: 한국석유공사 유가 정보 API
- **Google News RSS**: 뉴스 피드
- **JSON**: 데이터 저장 형식

## 📁 프로젝트 구조

```
program_hoho 4/
├── index.html              # 메인 페이지
├── pages/                  # 각 연료별 상세 페이지
│   ├── gasoline.html      # 휘발유 페이지
│   ├── high-octane.html   # 고급휘발유 페이지
│   ├── diesel.html        # 경유 페이지
│   └── lpg.html           # LPG 페이지
├── css/                    # 스타일시트
│   ├── main.css
│   └── prices.css
├── js/                     # JavaScript 파일
│   └── prices.js
├── backend/                # Flask 백엔드
│   ├── app.py             # Flask 애플리케이션
│   └── requirements.txt   # Python 의존성
├── api/                    # API 및 데이터 수집
│   ├── api.py             # API 유틸리티
│   ├── update_oil_prices.py  # 유가 데이터 업데이트 스크립트
│   ├── oil_prices_sido.ipynb  # 데이터 분석 노트북
│   └── data/              # 데이터 파일
│       ├── gasoline_prices_sido.json
│       └── oil_prices_sido.json
└── README.md
```

## 🚀 설치 및 실행 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd program_hoho\ 4
```

### 2. 백엔드 설정

```bash
cd backend
pip install -r requirements.txt
python app.py
```

백엔드 서버가 `http://localhost:5000`에서 실행됩니다.

### 3. 프론트엔드 실행

프로젝트는 정적 웹사이트이므로 웹 서버를 통해 실행하거나 직접 브라우저에서 열 수 있습니다.

#### 방법 1: Python 내장 서버 사용
```bash
python -m http.server 8000
```

#### 방법 2: Node.js http-server 사용
```bash
npx http-server -p 8000
```

브라우저에서 `http://localhost:8000`으로 접속합니다.

### 4. API 키 설정

다음 API 키가 필요합니다:
- **Google Maps API Key**: `index.html` 및 `pages/gasoline.html`에 설정
- **OPINET API Key**: `api/update_oil_prices.py` 및 `backend/app.py`에 설정
- **Naver Maps API Key**: `pages/diesel.html`에 설정 (선택사항)

## 📊 데이터 업데이트

유가 데이터를 업데이트하려면:

```bash
cd api
python update_oil_prices.py
```

이 스크립트는 OPINET API에서 최신 유가 정보를 가져와 `data/oil_prices_sido.json` 파일을 업데이트합니다.

## 🎨 주요 화면

### 메인 페이지
- Oil Today® 브랜드 소개
- 4가지 연료 타입 선택 (휘발유, 고급휘발유, LPG, 경유)
- 현재 위치 표시
- 유가 관련 뉴스 피드

### 연료별 상세 페이지
- 지역별 가격 정보 카드
- 가격 변동 추이 차트
- 주변 주유소 지도
- 전국 평균 및 주요 지역 가격 비교

## 🔧 개발 환경

- Python 3.7+
- Flask 2.0.1
- Modern Web Browser (Chrome, Firefox, Safari, Edge)
- 인터넷 연결 (API 호출 필요)

## 📝 라이선스

이 프로젝트는 한남대학교 프로그램호환 수업 프로젝트입니다.

## 🙏 감사의 말

- 한국석유공사 OPINET API
- Google Maps Platform
- Naver Cloud Platform

## 📞 문의

프로젝트 관련 문의사항이 있으시면 이슈를 등록해주세요.

---

**Made with ❤️ by 한남대학교 프로그램호환 팀**

