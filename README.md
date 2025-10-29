<div align="center">

# 🏢 세종시 상가 공실률 예측 프로젝트

### Commercial Vacancy Rate Prediction in Sejong City

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Archived-yellow.svg)]()
[![Competition](https://img.shields.io/badge/Competition-COMPAS%202024-red.svg)]()

**머신러닝과 시계열 분석을 활용한 상가 공실률 예측 및 원인 분석**

[프로젝트 개요](#-프로젝트-개요) •
[주요 기능](#-주요-기능) •
[빠른 시작](#-빠른-시작) •
[문서](#-문서) •
[결과](#-주요-결과)

</div>

---

## 📋 목차

- [프로젝트 개요](#-프로젝트-개요)
- [주요 기능](#-주요-기능)
- [프로젝트 구조](#-프로젝트-구조)
- [빠른 시작](#-빠른-시작)
  - [필수 요구사항](#필수-요구사항)
  - [설치](#설치)
  - [샘플 데이터 생성](#샘플-데이터-생성)
  - [사용 예제](#사용-예제)
- [문서](#-문서)
  - [분석 워크플로우](#분석-워크플로우)
  - [API 레퍼런스](#api-레퍼런스)
- [주요 결과](#-주요-결과)
- [데이터](#-데이터)
- [기술 스택](#-기술-스택)
- [문제 해결](#-문제-해결)
- [기여](#-기여)
- [라이선스](#-라이선스)
- [연락처](#-연락처)

---

## 🎯 프로젝트 개요

본 프로젝트는 **세종시 상가의 공실률 문제 해결**을 목표로 진행된 데이터 분석 프로젝트입니다.

### 배경

세종시는 행정중심복합도시로 개발되면서 급속한 인구 증가와 함께 상가 공실률 문제가 대두되었습니다. 이에 따라 현재 공실률을 정확히 파악하고, 미래 공실률을 예측하여 정책적 대응 방안을 마련할 필요성이 제기되었습니다.

### 목표

1. **월별/필지 단위 공실률 산출**: 세종시 상가의 현재 공실률을 정밀하게 계산
2. **공실률 예측**: ARIMA, SARIMA, Prophet 등을 활용한 2025년까지 18개월 예측
3. **원인 분석**: Random Forest의 Feature Importance를 통한 공실률 영향 요인 분석
4. **정책 제안**: 데이터 기반 공실률 저감 전략 수립

### 프로젝트 기간

- **2024년 COMPAS 공모전** 참여작

---

## ✨ 주요 기능

### 📊 데이터 분석

- **전처리**: 상가 개폐업 정보, 건축물 대장, 지도 데이터 통합 및 정제
- **공실률 산출**: 월별/필지 단위 정밀 공실률 계산
- **공간 분석**: GeoJSON 기반 지도 데이터 분석

### 🔮 예측 모델링

- **시계열 예측**: ARIMA, SARIMA, Prophet 모델
- **머신러닝**: Random Forest, Gradient Boosting
- **특성 엔지니어링**: BRT 노선 거리, 공시지가, 인구 데이터 등

### 📈 시각화

- **추세 분석**: 공실률 변화 추이 그래프
- **지도 기반**: 공간 분포 시각화
- **특성 중요도**: Feature Importance 및 Partial Dependence Plot

### 🛠️ 모듈화된 코드

- **재사용 가능한 함수**: `src/` 디렉토리의 모듈화된 코드
- **체계적인 구조**: 유형별로 분류된 Jupyter 노트북
- **샘플 데이터**: 테스트용 샘플 데이터 생성 도구

---

## 📁 프로젝트 구조

```
commercial-vacancy-prediction/
│
├── 📂 data/                          # 데이터 디렉토리
│   └── sample/                       # 샘플 데이터
│       ├── generate_sample_data.py   # 샘플 데이터 생성 스크립트
│       └── README.md                 # 샘플 데이터 설명
│
├── 📂 notebooks/                     # Jupyter 노트북
│   ├── 00_example_module_usage.ipynb # 모듈 사용 예제 ⭐
│   │
│   ├── 📂 01_preprocessing/          # 데이터 전처리
│   │   ├── 01_commercial_data_preprocessing.ipynb
│   │   ├── 02_map_data_preprocessing.ipynb
│   │   └── 03_building_store_preprocessing.ipynb
│   │
│   ├── 📂 02_analysis/               # 공실률 분석
│   │   ├── 01_close_rate_analysis.ipynb
│   │   └── 02_vacancy_rate_calculation.ipynb
│   │
│   ├── 📂 03_modeling/               # 예측 모델링
│   │   ├── 01_vacancy_prediction_timeseries.ipynb
│   │   ├── 02_random_forest_model.ipynb
│   │   └── 03_feature_engineering.ipynb
│   │
│   └── 📂 04_visualization/          # 시각화
│       ├── 01_vacancy_rate_visualization.ipynb
│       └── 02_rent_analysis.ipynb
│
├── 📂 src/                           # Python 모듈
│   ├── __init__.py
│   ├── config.py                     # 환경 설정 및 상수
│   ├── data_processing.py            # 데이터 전처리 함수
│   ├── visualization.py              # 시각화 함수
│   └── modeling.py                   # 모델링 함수
│
├── 📄 .gitignore                     # Git 제외 파일
├── 📄 README.md                      # 프로젝트 문서 (이 파일)
└── 📄 requirements.txt               # 필요 패키지 목록
```

---

## 🚀 빠른 시작

### 필수 요구사항

- **Python**: 3.8 이상
- **OS**: Linux, macOS, Windows
- **메모리**: 최소 4GB RAM 권장
- **디스크**: 최소 1GB 여유 공간

### 설치

#### 1. 저장소 클론

```bash
git clone https://github.com/jaesi/commercial-vacancy-prediction.git
cd commercial-vacancy-prediction
```

#### 2. 가상환경 생성 (권장)

```bash
# venv 사용
python -m venv venv

# 활성화 (Linux/macOS)
source venv/bin/activate

# 활성화 (Windows)
venv\Scripts\activate
```

#### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 샘플 데이터 생성

실제 데이터는 비공개이므로 샘플 데이터를 생성합니다:

```bash
cd data/sample
python generate_sample_data.py
cd ../..
```

생성되는 파일:
- `sample_commercial_data.geojson` - 상가 개폐업 정보
- `sample_building_data.geojson` - 건축물 정보
- `sample_population_data.csv` - 거주인구
- `sample_floating_population.csv` - 유동인구
- `sample_card_sales.csv` - 카드 매출
- `sample_land_price.csv` - 공시지가
- `sample_transport.csv` - 대중교통
- `sample_boundary.geojson` - 구역 경계

### 사용 예제

#### Jupyter Notebook 실행

```bash
jupyter notebook
```

브라우저에서 `notebooks/00_example_module_usage.ipynb`를 열어 모듈 사용법을 확인하세요.

#### Python 스크립트에서 모듈 사용

```python
# 1. 환경 설정
from src.config import setup_environment
setup_environment()

# 2. 데이터 전처리
from src.data_processing import check_franchise, calculate_vacancy_rate

franchise = check_franchise("스타벅스 세종점")  # 프랜차이즈 체크
vacancy_rate = calculate_vacancy_rate(100, 75)  # 공실률 계산

# 3. 시각화
from src.visualization import plot_vacancy_trend
import pandas as pd

df = pd.DataFrame({
    'date': pd.date_range('2020-01', '2024-05', freq='MS'),
    'vacancy_rat': [20, 22, 19, ...]  # 공실률 데이터
})
plot_vacancy_trend(df)

# 4. 모델링
from src.modeling import train_random_forest, evaluate_model

model = train_random_forest(X_train, y_train)
results = evaluate_model(model, X_test, y_test)
```

---

## 📚 문서

### 분석 워크플로우

#### 1️⃣ 데이터 전처리 (`notebooks/01_preprocessing/`)

**목적**: 원시 데이터를 분석 가능한 형태로 변환

- **상가 데이터 전처리** (`01_commercial_data_preprocessing.ipynb`)
  - 개폐업 정보 정제
  - 프랜차이즈 식별
  - 면적 결측치 처리

- **지도 데이터 전처리** (`02_map_data_preprocessing.ipynb`)
  - GeoJSON 파일 로드 및 검증
  - 공간 조인 (Spatial Join)
  - 좌표계 변환

- **건축물 데이터 전처리** (`03_building_store_preprocessing.ipynb`)
  - 건축물 대장 통합
  - 상가 정보 병합
  - 불필요한 업종 제거

#### 2️⃣ 공실률 분석 (`notebooks/02_analysis/`)

**목적**: 현재 공실률 산출 및 패턴 분석

- **공실률 산출** (`02_vacancy_rate_calculation.ipynb`)
  - 월별 영업/폐업 상태 추적
  - 필지 단위 집계
  - 공실률 계산식: `(전체 호실 수 - 영업 중 호실 수) / 전체 호실 수 × 100`

- **공실률 변화 분석** (`01_close_rate_analysis.ipynb`)
  - 시계열 패턴 탐색
  - 계절성 분석
  - 이상치 탐지

#### 3️⃣ 예측 모델링 (`notebooks/03_modeling/`)

**목적**: 미래 공실률 예측 및 영향 요인 분석

- **시계열 예측** (`01_vacancy_prediction_timeseries.ipynb`)
  - **ARIMA**: 자기회귀 이동평균 모델
  - **SARIMA**: 계절성 고려
  - **Prophet**: Facebook의 시계열 라이브러리

- **머신러닝 모델** (`02_random_forest_model.ipynb`)
  - Random Forest Regressor
  - Gradient Boosting
  - 하이퍼파라미터 튜닝

- **특성 엔지니어링** (`03_feature_engineering.ipynb`)
  - BRT 노선 거리 계산
  - 공시지가 데이터 병합
  - 대중교통 접근성 지표

#### 4️⃣ 시각화 (`notebooks/04_visualization/`)

**목적**: 분석 결과의 시각적 표현

- **공실률 시각화** (`01_vacancy_rate_visualization.ipynb`)
  - 지도 기반 시각화
  - 추세 그래프
  - 애니메이션 (선택사항)

- **임대료 분석** (`02_rent_analysis.ipynb`)
  - 임대료와 공실률 관계
  - 지역별 비교
  - 보증금/월세 분석

### API 레퍼런스

#### `src.config`

```python
setup_environment()
```
환경 설정을 초기화합니다 (한글 폰트, pandas 옵션 등).

**상수**:
- `FRANCHISE_LIST`: 프랜차이즈 리스트
- `DATE_RANGE_START`, `DATE_RANGE_END`: 분석 기간

#### `src.data_processing`

```python
check_franchise(name, franchise_list=FRANCHISE_LIST)
```
상가명에서 프랜차이즈 여부를 확인합니다.

```python
calculate_vacancy_rate(total_rooms, occupied_rooms)
```
공실률을 계산합니다 (%).

```python
fill_missing_area(df, group_col='rd_addr_left', area_col='plc_area')
```
결측된 면적을 그룹별 중위값으로 채웁니다.

```python
pnu_to_frame(df)
```
필지 단위로 월별 데이터를 집계합니다.

#### `src.visualization`

```python
plot_vacancy_trend(df, date_col='date', vacancy_col='vacancy_rat', ...)
```
공실률 추이를 시각화합니다.

```python
plot_prediction(observed_data, predicted_data, ...)
```
관측값과 예측값을 함께 표시합니다.

```python
plot_feature_importance(feature_names, importances, top_n=None, ...)
```
특성 중요도를 시각화합니다.

```python
plot_spatial_data(gdf, boundary_gdf=None, column=None, ...)
```
공간 데이터를 지도에 표시합니다.

#### `src.modeling`

```python
split_data(X, y, test_size=0.15, random_state=42)
```
데이터를 학습/테스트 세트로 분할합니다.

```python
train_random_forest(X_train, y_train, params=None, random_search=False)
```
Random Forest 모델을 학습합니다.

```python
train_arima(data, order=(10, 1, 5), steps=19)
```
ARIMA 모델로 시계열을 예측합니다.

```python
evaluate_model(model, X_test, y_test)
```
모델 성능을 평가합니다 (MSE, RMSE, R²).

---

## 📊 주요 결과

### 시계열 예측 성능

| 모델 | MSE | RMSE | R² |
|------|-----|------|-----|
| **ARIMA** | 121.21 | 11.01 | 0.744 |
| **SARIMA** | - | - | - |
| **Prophet** | - | - | - |

### 머신러닝 모델 성능

| 모델 | RMSE | R² | 비고 |
|------|------|-----|------|
| **Random Forest** | 7.39 | 0.885 | 최적화 후 |
| **Gradient Boosting** | 11.01 | 0.744 | 기본 파라미터 |

### 공실률 영향 요인 (Feature Importance)

| 순위 | 특성 | 중요도 | 설명 |
|------|------|--------|------|
| 1 | 건폐율 (bc_rat) | 15.5% | 건축면적/대지면적 비율 |
| 2 | 건물 높이 (height) | 12.4% | 건물 높이 (m) |
| 3 | 거주인구 (res_pop) | 8.6% | 해당 지역 거주인구 |
| 4 | 건축면적 (arch_area) | 8.2% | 건축 연면적 |
| 5 | 중심지 거리 (distance_to_center) | 6.7% | 세종시 중심부로부터 거리 |
| 6 | BRT 거리 (brt_distance) | 6.7% | 가장 가까운 BRT 정류장 거리 |
| 7 | 유동인구 (floating_pop) | 6.6% | 해당 지역 유동인구 |
| 8 | 음식 매출 (card_f&b) | 5.4% | 음식 업종 카드 매출액 |

### 주요 인사이트

1. **건폐율이 가장 중요한 요인**: 건폐율이 높을수록 공실률이 낮은 경향
2. **고층 건물의 공실률 증가**: 층수가 높을수록 공실률 상승
3. **거주인구의 영향**: 거주인구가 많을수록 공실률 감소
4. **대중교통 접근성**: BRT 노선과의 거리가 가까울수록 공실률 낮음

---

## 💾 데이터

### 실제 데이터 (비공개)

이 프로젝트는 다음 공모전 내부 데이터를 사용했습니다:

- **상가 개폐업 정보**: 세종시 전체 상가의 개업/폐업 이력
- **건축물 대장**: 건물 정보, 용도, 면적 등
- **거주인구 및 유동인구**: 행정동별 인구 통계
- **카드 매출 데이터**: 업종별 카드 결제 금액
- **공시지가**: 연도별 토지 공시지가
- **대중교통 정보**: 버스, BRT 정류장 위치

⚠️ **데이터 사용 제한**: 실제 데이터는 공모전 규정에 따라 공개되지 않습니다.

### 샘플 데이터

코드 구조 및 분석 방법론 이해를 위한 샘플 데이터가 제공됩니다:

```bash
cd data/sample
python generate_sample_data.py
```

**주의**: 샘플 데이터는 실제 분석 결과와 다를 수 있습니다.

---

## 🔧 기술 스택

### 언어 및 프레임워크

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

### 데이터 처리

- **pandas**: 데이터 조작 및 분석
- **numpy**: 수치 연산
- **geopandas**: 공간 데이터 처리
- **shapely**: 기하학적 객체 처리

### 시각화

- **matplotlib**: 기본 그래프
- **seaborn**: 통계 시각화

### 머신러닝

- **scikit-learn**: Random Forest, Gradient Boosting
- **statsmodels**: ARIMA, SARIMA
- **prophet**: Facebook의 시계열 예측 라이브러리

### 개발 환경

- **Git**: 버전 관리
- **Jupyter Notebook**: 대화형 분석

---

## 🐛 문제 해결

### 자주 묻는 질문 (FAQ)

#### Q1. 한글이 깨져서 나옵니다.

**A**: `src.config.setup_environment()`를 호출하여 한글 폰트를 설정하세요.

```python
from src.config import setup_environment
setup_environment()
```

Windows의 경우 '맑은 고딕', Mac의 경우 'AppleGothic' 폰트가 설치되어 있어야 합니다.

#### Q2. 샘플 데이터 생성 시 에러가 발생합니다.

**A**: 필요한 패키지가 모두 설치되었는지 확인하세요.

```bash
pip install pandas numpy geopandas shapely
cd data/sample
python generate_sample_data.py
```

#### Q3. 모듈을 import할 수 없습니다.

**A**: Python 경로에 프로젝트 루트를 추가하세요.

```python
import sys
sys.path.append('../..')  # 노트북이 notebooks/ 하위에 있는 경우
```

#### Q4. ARIMA 모델이 수렴하지 않습니다.

**A**: 데이터의 정상성(stationarity)을 확인하고, 차수를 조정하세요.

```python
from statsmodels.tsa.stattools import adfuller

# 정상성 검정
result = adfuller(data)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')

# p-value > 0.05이면 차분 필요
```

### 알려진 이슈

- **대용량 데이터**: 메모리 부족 시 데이터를 청크로 나눠서 처리
- **GeoJSON 렌더링**: 일부 환경에서 지도 렌더링이 느릴 수 있음

---

## 🤝 기여

본 프로젝트는 2024 COMPAS 공모전을 위해 개발되어 현재 **아카이브 상태**입니다.

### 코드 재사용

이 코드를 자유롭게 사용할 수 있습니다:

1. 프로젝트를 Fork
2. 데이터 경로를 자신의 환경에 맞게 수정
3. 필요에 따라 코드 수정 및 개선

### 개선 제안

이슈를 통해 버그 리포트나 개선 제안을 환영합니다!

---

## 📜 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

### 주의사항

- ⚠️ **데이터**: 실제 공모전 데이터는 비공개이며 공개할 수 없습니다
- ⚠️ **샘플 데이터**: 제공된 샘플 데이터는 실제 분석 결과와 다를 수 있습니다
- ⚠️ **코드 재사용**: 실제 프로젝트에 사용 시 데이터 경로를 적절히 수정하세요

---

## 📞 연락처

프로젝트 관련 문의사항이 있으시면 GitHub Issues를 통해 연락해주세요.

- **GitHub**: [jaesi/commercial-vacancy-prediction](https://github.com/jaesi/commercial-vacancy-prediction)
- **Issues**: [이슈 등록](https://github.com/jaesi/commercial-vacancy-prediction/issues)

---

## 🙏 감사의 말

이 프로젝트는 2024 COMPAS 공모전을 통해 진행되었습니다.

---

## 📌 업데이트 내역

### v2.0.0 (2024-10-29)
- 🎨 프로젝트 아카이빙 및 대대적인 코드 정리
- 📁 노트북 파일 유형별 분류 및 재구성
- 🔧 공통 함수 모듈화 (`src/` 디렉토리)
- 📝 모듈 사용 예제 노트북 추가
- 🗂️ 샘플 데이터 생성 스크립트 제공
- 📖 README 구조적 개선 및 문서화

### v1.0.0 (2024-10)
- 🚀 초기 버전 (공모전 제출)
- 📊 공실률 분석 및 예측 모델 구현

---

<div align="center">

**[⬆ 맨 위로 돌아가기](#-세종시-상가-공실률-예측-프로젝트)**

Made with ❤️ for COMPAS 2024

</div>
