# 샘플 데이터 설명

이 디렉토리에는 공모전 실제 데이터를 대체하는 샘플 데이터가 포함되어 있습니다.

## 데이터 생성 방법

```bash
cd data/sample
python generate_sample_data.py
```

## 샘플 데이터 파일 목록

### 1. sample_commercial_data.geojson
- **설명**: 상가 개폐업 정보 샘플 데이터
- **주요 컬럼**:
  - `bplc_nm`: 상가명
  - `service_nm`: 업종
  - `lcpmt_dt`: 개업일
  - `cls_date`: 폐업일
  - `biz_stts_cd`: 영업 상태 코드 (1: 영업, 3: 폐업)
  - `plc_area`: 면적
  - `rd_addr`: 도로명 주소
  - `geometry`: 위치 정보

### 2. sample_building_data.geojson
- **설명**: 건축물 대장 샘플 데이터
- **주요 컬럼**:
  - `buld_nm`: 건물명
  - `main_purps_cd_nm`: 주용도
  - `arch_area`: 건축면적
  - `bc_rat`: 건폐율
  - `tot_area`: 연면적
  - `heit`: 높이
  - `use_apr_day`: 사용승인일
  - `geometry`: 위치 정보

### 3. sample_population_data.csv
- **설명**: 거주인구 샘플 데이터
- **주요 컬럼**:
  - `rd_addr`: 도로명 주소
  - `year`: 년도
  - `거주인구_총합`: 거주인구 수

### 4. sample_floating_population.csv
- **설명**: 유동인구 샘플 데이터
- **주요 컬럼**:
  - `rd_addr`: 도로명 주소
  - `년도`: 년도
  - `유동인구_총합`: 유동인구 수

### 5. sample_card_sales.csv
- **설명**: 카드 매출 샘플 데이터
- **주요 컬럼**:
  - `rd_addr`: 도로명 주소
  - `KBC_BZC_NM_1`: 업종 구분
  - `CARD_SALES`: 카드 매출액
  - `EST_SALES`: 추정 매출액

### 6. sample_land_price.csv
- **설명**: 공시지가 샘플 데이터
- **주요 컬럼**:
  - `rd_addr`: 도로명 주소
  - `2020` ~ `2024`: 연도별 공시지가

### 7. sample_transport.csv
- **설명**: 대중교통 샘플 데이터
- **주요 컬럼**:
  - `rd_addr`: 도로명 주소
  - `type`: 교통 유형 (bus, byc, BRT)
  - `대중교통_총합`: 대중교통 수

### 8. sample_boundary.geojson
- **설명**: 세종시 대상구역 경계 샘플 데이터
- **주요 컬럼**:
  - `name`: 구역명
  - `geometry`: 경계 다각형

## 주의사항

⚠️ **이 데이터는 실제 공모전 데이터가 아닌 임의로 생성된 샘플 데이터입니다.**
- 실제 분석 결과와 다를 수 있습니다.
- 코드 구조 및 분석 방법론 이해를 위한 용도로만 사용하세요.
- 실제 프로젝트에 사용할 경우 실제 데이터로 교체해야 합니다.
