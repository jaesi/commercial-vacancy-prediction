"""
샘플 데이터 생성 스크립트
실제 공모전 데이터를 대체하는 샘플 데이터를 생성합니다.
"""

import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon
from datetime import datetime, timedelta

np.random.seed(42)

def generate_sample_commercial_data(n_samples=100):
    """상가 개폐업 샘플 데이터 생성"""

    # 세종시 대략적인 좌표 범위
    lon_range = (127.23, 127.29)
    lat_range = (36.48, 36.53)

    # 행정동 리스트
    emd_list = ['고운동', '나성동', '다정동', '어진동', '보람동', '새롬동', '소담동', '아름동', '해밀동', '한솔동']

    # 업종 리스트
    service_types = ['일반음식점', '휴게음식점', '제과점', '커피숍', '편의점', '미용실', '의류판매', '학원']

    data = []
    for i in range(n_samples):
        # 개업일 (2015-2023년 사이)
        open_date = datetime(2015, 1, 1) + timedelta(days=np.random.randint(0, 365*8))

        # 영업 상태 (70% 영업, 30% 폐업)
        biz_status = np.random.choice([1, 3], p=[0.7, 0.3])

        # 폐업일 (폐업인 경우)
        close_date = None
        if biz_status == 3:
            close_date = open_date + timedelta(days=np.random.randint(180, 1800))

        data.append({
            'bplc_nm': f'샘플상가{i}',
            'service_nm': np.random.choice(service_types),
            'lcpmt_dt': open_date.strftime('%Y-%m-%d'),
            'cls_date': close_date.strftime('%Y-%m-%d') if close_date else None,
            'biz_stts_cd': biz_status,
            'biz_stts_nm': '영업/정상' if biz_status == 1 else '폐업',
            'plc_area': np.random.uniform(20, 200),
            'lon': np.random.uniform(*lon_range),
            'lat': np.random.uniform(*lat_range),
            'emd_nm': np.random.choice(emd_list),
            'rd_addr': f'세종특별자치시 샘플로 {np.random.randint(1, 500)}',
            'addr': f'세종특별자치시 {np.random.choice(emd_list)} {np.random.randint(1, 1000)}'
        })

    df = pd.DataFrame(data)

    # GeoDataFrame으로 변환
    geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    return gdf


def generate_sample_building_data(n_samples=50):
    """건축물 대장 샘플 데이터 생성"""

    lon_range = (127.23, 127.29)
    lat_range = (36.48, 36.53)

    building_types = ['제1종근린생활시설', '제2종근린생활시설', '판매시설', '업무시설']

    data = []
    for i in range(n_samples):
        data.append({
            'buld_nm': f'샘플건물{i}' if np.random.random() > 0.3 else None,
            'plat_plc': f'세종특별자치시 샘플동 {np.random.randint(1, 2000)}번지',
            'new_plat_plc': f'세종특별자치시 샘플로 {np.random.randint(1, 500)}',
            'main_purps_cd_nm': np.random.choice(building_types),
            'plat_area': np.random.uniform(100, 5000),
            'arch_area': np.random.uniform(100, 2000),
            'bc_rat': np.random.uniform(50, 90),
            'tot_area': np.random.uniform(500, 50000),
            'heit': np.random.uniform(10, 70),
            'grnd_flr_cnt': np.random.randint(1, 20),
            'ugrnd_flr_cnt': np.random.randint(0, 3),
            'use_apr_day': (datetime(2010, 1, 1) + timedelta(days=np.random.randint(0, 365*13))).strftime('%Y-%m-%d'),
            'lon': np.random.uniform(*lon_range),
            'lat': np.random.uniform(*lat_range)
        })

    df = pd.DataFrame(data)
    geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    return gdf


def generate_sample_population_data():
    """인구 데이터 샘플 생성"""

    addresses = [f'세종특별자치시 샘플로 {i}' for i in range(1, 101)]
    years = [2020, 2021, 2022, 2023]

    data = []
    for addr in addresses:
        for year in years:
            data.append({
                'rd_addr': addr,
                'year': year,
                '거주인구_총합': np.random.randint(500, 15000)
            })

    return pd.DataFrame(data)


def generate_sample_floating_population():
    """유동인구 데이터 샘플 생성"""

    addresses = [f'세종특별자치시 샘플로 {i}' for i in range(1, 101)]
    years = [2020, 2021, 2022, 2023]

    data = []
    for addr in addresses:
        for year in years:
            data.append({
                'rd_addr': addr,
                '년도': year,
                '유동인구_총합': np.random.randint(10000, 1000000)
            })

    return pd.DataFrame(data)


def generate_sample_card_sales():
    """카드 매출 데이터 샘플 생성"""

    addresses = [f'세종특별자치시 샘플로 {i}' for i in range(1, 101)]
    business_types = ['음식', '소매업', '서비스', '기타']

    data = []
    for addr in addresses:
        for biz_type in business_types:
            if np.random.random() > 0.3:  # 70% 확률로 데이터 생성
                data.append({
                    'rd_addr': addr,
                    'KBC_BZC_NM_1': biz_type,
                    'CARD_SALES': np.random.uniform(1000000, 500000000),
                    'EST_SALES': np.random.uniform(100000, 5000000)
                })

    return pd.DataFrame(data)


def generate_sample_land_price():
    """공시지가 데이터 샘플 생성"""

    addresses = [f'세종특별자치시 샘플로 {i}' for i in range(1, 101)]
    years = [2020, 2021, 2022, 2023, 2024]

    data = []
    for addr in addresses:
        base_price = np.random.uniform(1000000, 5000000)
        row = {'rd_addr': addr}
        for year in years:
            # 매년 약간씩 증가
            row[str(year)] = base_price * (1 + np.random.uniform(0.01, 0.1)) ** (year - 2020)
        data.append(row)

    return pd.DataFrame(data)


def generate_sample_transport():
    """대중교통 데이터 샘플 생성"""

    addresses = [f'세종특별자치시 샘플로 {i}' for i in range(1, 51)]
    transport_types = ['bus', 'byc', 'BRT']

    data = []
    for addr in addresses:
        if np.random.random() > 0.5:  # 50% 확률로 대중교통 존재
            data.append({
                'rd_addr': addr,
                'type': np.random.choice(transport_types),
                '대중교통_총합': np.random.randint(1, 5)
            })

    return pd.DataFrame(data)


def generate_sample_boundary():
    """세종시 대상구역 경계 샘플 데이터 생성"""

    # 간단한 사각형 경계
    coords = [
        (127.23, 36.48),
        (127.29, 36.48),
        (127.29, 36.53),
        (127.23, 36.53),
        (127.23, 36.48)
    ]

    polygon = Polygon(coords)
    gdf = gpd.GeoDataFrame({'name': ['세종시 대상구역']}, geometry=[polygon], crs='EPSG:4326')

    return gdf


if __name__ == '__main__':
    print("샘플 데이터 생성 중...")

    # 1. 상가 데이터
    commercial_gdf = generate_sample_commercial_data(200)
    commercial_gdf.to_file('sample_commercial_data.geojson', driver='GeoJSON')
    print("✓ 상가 데이터 생성 완료")

    # 2. 건축물 데이터
    building_gdf = generate_sample_building_data(100)
    building_gdf.to_file('sample_building_data.geojson', driver='GeoJSON')
    print("✓ 건축물 데이터 생성 완료")

    # 3. 인구 데이터
    population_df = generate_sample_population_data()
    population_df.to_csv('sample_population_data.csv', index=False, encoding='utf-8-sig')
    print("✓ 인구 데이터 생성 완료")

    # 4. 유동인구 데이터
    floating_pop_df = generate_sample_floating_population()
    floating_pop_df.to_csv('sample_floating_population.csv', index=False, encoding='utf-8-sig')
    print("✓ 유동인구 데이터 생성 완료")

    # 5. 카드 매출 데이터
    card_sales_df = generate_sample_card_sales()
    card_sales_df.to_csv('sample_card_sales.csv', index=False, encoding='utf-8-sig')
    print("✓ 카드 매출 데이터 생성 완료")

    # 6. 공시지가 데이터
    land_price_df = generate_sample_land_price()
    land_price_df.to_csv('sample_land_price.csv', index=False, encoding='utf-8-sig')
    print("✓ 공시지가 데이터 생성 완료")

    # 7. 대중교통 데이터
    transport_df = generate_sample_transport()
    transport_df.to_csv('sample_transport.csv', index=False, encoding='utf-8-sig')
    print("✓ 대중교통 데이터 생성 완료")

    # 8. 경계 데이터
    boundary_gdf = generate_sample_boundary()
    boundary_gdf.to_file('sample_boundary.geojson', driver='GeoJSON')
    print("✓ 경계 데이터 생성 완료")

    print("\n모든 샘플 데이터 생성 완료!")
    print("생성된 파일들:")
    print("  - sample_commercial_data.geojson")
    print("  - sample_building_data.geojson")
    print("  - sample_population_data.csv")
    print("  - sample_floating_population.csv")
    print("  - sample_card_sales.csv")
    print("  - sample_land_price.csv")
    print("  - sample_transport.csv")
    print("  - sample_boundary.geojson")
