"""
Data processing module
데이터 전처리 모듈
"""

import pandas as pd
import numpy as np
import geopandas as gpd
from .config import FRANCHISE_LIST, DATE_RANGE_START, DATE_RANGE_END


def check_franchise(name, franchise_list=FRANCHISE_LIST):
    """
    상가명에서 프랜차이즈 여부를 확인합니다.

    Parameters:
    -----------
    name : str
        상가명
    franchise_list : list
        프랜차이즈 리스트

    Returns:
    --------
    int : 프랜차이즈면 1, 아니면 0
    """
    if pd.isna(name):
        return 0
    return 1 if any(f in name for f in franchise_list) else 0


def set_franchise(row):
    """
    프랜차이즈 영업 기간을 월별로 표시합니다.

    Parameters:
    -----------
    row : pandas.Series
        데이터프레임의 한 행

    Returns:
    --------
    pandas.Series : 월별 프랜차이즈 수가 업데이트된 행
    """
    month_list = pd.date_range(start=DATE_RANGE_START, end=DATE_RANGE_END, freq='MS').strftime('%Y-%m').tolist()

    if row['frnch'] == 1:
        if row['biz_stts_cd'] == 1:  # 영업 중
            open_months = pd.date_range(
                start=row['lcpmt_dt'] - pd.DateOffset(days=30),
                end=DATE_RANGE_END,
                freq='MS'
            ).strftime('%Y-%m').tolist()
            for month in open_months:
                if month in row.index:
                    row[month] = 1
        elif row['biz_stts_cd'] == 3:  # 폐업
            if pd.notna(row['cls_date']):
                open_months = pd.date_range(
                    start=row['lcpmt_dt'] - pd.DateOffset(days=30),
                    end=row['cls_date'],
                    freq='MS'
                ).strftime('%Y-%m').tolist()
                for month in open_months:
                    if month in row.index:
                        row[month] = 1
    return row


def set_monthly_values(row):
    """
    월별 영업 여부를 표시합니다 (공실률 계산용).

    Parameters:
    -----------
    row : pandas.Series
        데이터프레임의 한 행

    Returns:
    --------
    pandas.Series : 월별 영업 여부가 업데이트된 행
    """
    month_list = pd.date_range(start=DATE_RANGE_START, end=DATE_RANGE_END, freq='MS').strftime('%Y-%m').tolist()

    if row['biz_stts_cd'] == 1:  # 영업 중
        open_months = pd.date_range(
            start=row['lcpmt_dt'] - pd.DateOffset(days=30),
            end=DATE_RANGE_END,
            freq='MS'
        ).strftime('%Y-%m').tolist()
        for month in open_months:
            if month in row.index:
                row[month] = 1
    elif row['biz_stts_cd'] == 3:  # 폐업
        if pd.notna(row['cls_date']):
            open_months = pd.date_range(
                start=row['lcpmt_dt'] - pd.DateOffset(days=30),
                end=row['cls_date'],
                freq='MS'
            ).strftime('%Y-%m').tolist()
            for month in open_months:
                if month in row.index:
                    row[month] = 1
    return row


def set_monthly_area(row):
    """
    월별 영업 면적을 표시합니다.

    Parameters:
    -----------
    row : pandas.Series
        데이터프레임의 한 행

    Returns:
    --------
    pandas.Series : 월별 면적이 업데이트된 행
    """
    month_list = pd.date_range(start=DATE_RANGE_START, end=DATE_RANGE_END, freq='MS').strftime('%Y-%m').tolist()

    if row['biz_stts_cd'] == 1:  # 영업 중
        open_months = pd.date_range(
            start=row['lcpmt_dt'] - pd.DateOffset(days=30),
            end=DATE_RANGE_END,
            freq='MS'
        ).strftime('%Y-%m').tolist()
        for month in open_months:
            if month in row.index:
                row[month] = row['plc_area']
    elif row['biz_stts_cd'] == 3:  # 폐업
        if pd.notna(row['cls_date']):
            open_months = pd.date_range(
                start=row['lcpmt_dt'] - pd.DateOffset(days=30),
                end=row['cls_date'],
                freq='MS'
            ).strftime('%Y-%m').tolist()
            for month in open_months:
                if month in row.index:
                    row[month] = row['plc_area']
    return row


def pnu_to_frame(df):
    """
    필지 단위로 월별 데이터를 집계합니다.

    Parameters:
    -----------
    df : pandas.DataFrame or geopandas.GeoDataFrame
        필지별 상가 데이터

    Returns:
    --------
    geopandas.GeoDataFrame : 집계된 데이터
    """
    month_list = pd.date_range(start=DATE_RANGE_START, end=DATE_RANGE_END, freq='MS').strftime('%Y-%m').tolist()

    # 1. 프랜차이즈 수 연산
    temp_df = df.apply(lambda row: set_franchise(row), axis=1)
    total_frnchs = temp_df[month_list].sum(axis=0).to_frame()
    total_frnchs.columns = ["Tot_frnchs"]

    # 2. 호실 수 연산
    temp_df = df.apply(lambda row: set_monthly_values(row), axis=1)
    total_rooms = temp_df[month_list].sum(axis=0).to_frame()
    total_rooms.columns = ["Tot_Rooms"]

    # 3. 면적 연산
    temp_df = df.apply(lambda row: set_monthly_area(row), axis=1)
    total_area = temp_df[month_list].sum(axis=0).to_frame()
    total_area.columns = ["Tot_Area"]

    # 최종 데이터프레임 생성
    total_set = pd.concat([total_rooms, total_frnchs, total_area], axis=1)

    # 프랜차이즈 비율 계산
    total_set['frnch_ratio'] = total_set['Tot_frnchs'] / total_set['Tot_Rooms']
    total_set['frnch_ratio'] = total_set['frnch_ratio'].fillna(0)

    # geometry 추가 (GeoDataFrame인 경우)
    if isinstance(df, gpd.GeoDataFrame):
        geometry = df.iloc[0].geometry
        total_set['geometry'] = geometry
        total_set = gpd.GeoDataFrame(total_set, geometry='geometry')

    # 주소 추가
    if 'rd_addr_left' in df.columns:
        total_set['rd_addr'] = df.iloc[0]['rd_addr_left']

    return total_set


def calculate_vacancy_rate(total_rooms, occupied_rooms):
    """
    공실률을 계산합니다.

    Parameters:
    -----------
    total_rooms : int or float
        전체 호실 수
    occupied_rooms : int or float
        영업 중인 호실 수

    Returns:
    --------
    float : 공실률 (%)
    """
    if total_rooms == 0:
        return 0
    return ((total_rooms - occupied_rooms) / total_rooms) * 100


def fill_missing_area(df, group_col='rd_addr_left', area_col='plc_area'):
    """
    결측된 면적 값을 그룹별 중위값으로 채웁니다.

    Parameters:
    -----------
    df : pandas.DataFrame
        데이터프레임
    group_col : str
        그룹화할 컬럼명
    area_col : str
        면적 컬럼명

    Returns:
    --------
    pandas.DataFrame : 면적이 채워진 데이터프레임
    """
    df[area_col] = df.groupby(group_col)[area_col].transform(
        lambda x: x.fillna(x.median())
    )
    return df
