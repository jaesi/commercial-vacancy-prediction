# 세종시 상가 공실률 예측 프로젝트

## 프로젝트 개요

이 프로젝트는 세종시 상가의 공실률 문제 해결을 위해 현재 공실률 데이터를 월별/필지 단위로 산출하고, 향후 2025년까지 약 18개월의 공실률을 예측하였습니다. 또한 Random Forest의 Feature Importance와 Dependence Plot을 통해 공실률 원인을 분석하여 공실률 저감을 위한 전략을 제안하였습니다.

### 주요 기능

- **데이터 전처리**: 상가 개폐업, 건축물 대장, 지도 데이터 전처리
- **공실률 분석**: 월별/필지 단위 공실률 산출 및 시각화
- **시계열 예측**: ARIMA, SARIMA, Prophet 모델을 활용한 공실률 예측
- **머신러닝 모델링**: Random Forest, Gradient Boosting을 활용한 공실률 영향 요인 분석

---

## 프로젝트 구조

```
commercial-vacancy-prediction/
├── data/
│   └── sample/                    # 샘플 데이터 (실제 데이터는 비공개)
│       ├── generate_sample_data.py
│       ├── README.md
│       └── *.csv, *.geojson
│
├── notebooks/                     # Jupyter 노트북 (분석 과정)
│   ├── 01_preprocessing/          # 데이터 전처리
│   │   ├── 01_commercial_data_preprocessing.ipynb
│   │   ├── 02_map_data_preprocessing.ipynb
│   │   └── 03_building_store_preprocessing.ipynb
│   │
│   ├── 02_analysis/               # 데이터 분석
│   │   ├── 01_close_rate_analysis.ipynb
│   │   └── 02_vacancy_rate_calculation.ipynb
│   │
│   ├── 03_modeling/               # 모델링
│   │   ├── 01_vacancy_prediction_timeseries.ipynb
│   │   ├── 02_random_forest_model.ipynb
│   │   └── 03_feature_engineering.ipynb
│   │
│   └── 04_visualization/          # 시각화
│       ├── 01_vacancy_rate_visualization.ipynb
│       └── 02_rent_analysis.ipynb
│
├── src/                           # Python 모듈
│   ├── __init__.py
│   ├── config.py                  # 환경 설정
│   ├── data_processing.py         # 데이터 전처리 함수
│   ├── visualization.py           # 시각화 함수
│   └── modeling.py                # 모델링 함수
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 설치 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd commercial-vacancy-prediction
```

### 2. 가상환경 생성 (권장)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 샘플 데이터 생성

```bash
cd data/sample
python generate_sample_data.py
cd ../..
```

---

## 사용 방법

### Jupyter Notebook 실행

```bash
jupyter notebook
```

브라우저에서 `notebooks/` 디렉토리의 노트북을 순서대로 실행하세요.

### Python 모듈 사용 예제

```python
# 환경 설정
from src.config import setup_environment
setup_environment()

# 데이터 전처리
from src.data_processing import check_franchise, calculate_vacancy_rate
franchise_status = check_franchise("스타벅스 세종점")
vacancy_rate = calculate_vacancy_rate(total_rooms=100, occupied_rooms=75)

# 시각화
from src.visualization import plot_vacancy_trend
import pandas as pd

df = pd.read_csv('vacancy_data.csv')
plot_vacancy_trend(df, date_col='date', vacancy_col='vacancy_rat')

# 모델링
from src.modeling import train_random_forest, evaluate_model
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)
model = train_random_forest(X_train, y_train)
results = evaluate_model(model, X_test, y_test)
```

---

## 분석 워크플로우

### 1. 데이터 전처리 (`notebooks/01_preprocessing/`)

- **상가 데이터 전처리**: 개폐업 정보, 면적, 위치 정보 정제
- **지도 데이터 전처리**: GeoJSON 파일 처리 및 공간 조인
- **건축물 데이터 전처리**: 건축물 대장 및 상가 정보 병합

### 2. 공실률 분석 (`notebooks/02_analysis/`)

- **공실률 산출**: 월별/필지 단위 공실률 계산
- **공실률 변화 분석**: 시계열 패턴 분석 및 시각화

### 3. 예측 모델링 (`notebooks/03_modeling/`)

- **시계열 예측**: ARIMA, SARIMA, Prophet 모델
- **머신러닝 모델**: Random Forest, Gradient Boosting
- **특성 엔지니어링**: BRT 노선 거리, 공시지가 등 특성 추가

### 4. 시각화 (`notebooks/04_visualization/`)

- **공실률 시각화**: 지도 기반 시각화, 추세 그래프
- **임대료 분석**: 임대료와 공실률 관계 분석

---

## 주요 결과

### 1. 공실률 예측

- **ARIMA 모델**: MSE 121.21, R² 0.744
- **SARIMA 모델**: 계절성을 고려한 예측
- **Prophet 모델**: 추세 및 주기 패턴 분석

### 2. 공실률 영향 요인 (Random Forest Feature Importance)

1. 건폐율 (bc_rat): 15.5%
2. 건물 높이 (height): 12.4%
3. 거주인구 (res_pop): 8.6%
4. 건축면적 (arch_area): 8.2%
5. 중심지 거리 (distance_to_center): 6.7%

### 3. 모델 성능

- **Random Forest (최적화)**: RMSE 7.39, R² 0.885
- **Gradient Boosting**: RMSE 11.01, R² 0.744

---

## 데이터 정보

### 실제 데이터 (비공개)

실제 프로젝트에서는 다음 데이터를 사용했습니다:
- 세종시 상가 개폐업 정보
- 건축물 대장
- 거주인구 및 유동인구
- 카드 매출 데이터
- 공시지가 정보
- 대중교통 정보 (버스, BRT)

### 샘플 데이터

`data/sample/` 디렉토리에 샘플 데이터가 포함되어 있습니다. 이는 코드 구조 및 분석 방법론 이해를 위한 것으로, 실제 공모전 데이터가 아닙니다.

---

## 기술 스택

- **언어**: Python 3.8+
- **데이터 처리**: pandas, numpy, geopandas
- **시각화**: matplotlib, seaborn
- **머신러닝**: scikit-learn
- **시계열 분석**: statsmodels, prophet
- **공간 데이터**: shapely, geopandas

---

## 기여 및 라이선스

이 프로젝트는 2024 COMPAS 공모전을 위해 개발되었습니다.

### 주의사항

- 실제 데이터는 공모전 내부 자료로 공개되지 않습니다.
- 샘플 데이터는 실제 분석 결과와 다를 수 있습니다.
- 코드 재사용 시 데이터 경로를 적절히 수정해야 합니다.

---

## 문의

프로젝트 관련 문의사항이 있으시면 이슈를 등록해주세요.

---

## 업데이트 내역

- **2024-10**: 초기 버전 (공모전 제출)
- **2024-10**: 코드 아카이빙 및 정리
  - 노트북 파일 유형별 분류
  - 공통 함수 모듈화
  - 샘플 데이터 생성
  - README 개선
