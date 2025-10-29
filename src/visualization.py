"""
Visualization module
시각화 모듈
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd


def plot_vacancy_trend(df, date_col='date', vacancy_col='vacancy_rat',
                       figsize=(16, 6), dpi=300, title='공실률 변화 추이'):
    """
    공실률 추이를 시각화합니다.

    Parameters:
    -----------
    df : pandas.DataFrame
        데이터프레임
    date_col : str
        날짜 컬럼명
    vacancy_col : str
        공실률 컬럼명
    figsize : tuple
        그래프 크기
    dpi : int
        해상도
    title : str
        그래프 제목
    """
    plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(df[date_col], df[vacancy_col], linewidth=3, color='darkred')
    plt.title(title, loc='left', fontsize=20, fontweight='bold', pad=20)
    plt.xlabel('날짜(월)', fontsize=15, labelpad=15)
    plt.ylabel('공실률(%)', fontsize=15, labelpad=15)

    # 스타일 설정
    ax = plt.gca()
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(axis='y', color='black', alpha=0.5)
    plt.ylim(10, 40)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_prediction(observed_data, predicted_data,
                   date_col='date', value_col='vacancy_rat',
                   pred_col='mean', ci_lower=None, ci_upper=None,
                   figsize=(16, 6), dpi=300, title='공실률 예측'):
    """
    관측값과 예측값을 함께 시각화합니다.

    Parameters:
    -----------
    observed_data : pandas.DataFrame
        관측 데이터
    predicted_data : pandas.DataFrame
        예측 데이터
    date_col : str
        날짜 컬럼명
    value_col : str
        관측값 컬럼명
    pred_col : str
        예측값 컬럼명
    ci_lower : str
        신뢰구간 하한 컬럼명
    ci_upper : str
        신뢰구간 상한 컬럼명
    figsize : tuple
        그래프 크기
    dpi : int
        해상도
    title : str
        그래프 제목
    """
    plt.figure(figsize=figsize, dpi=dpi)

    # 관측값
    if isinstance(observed_data.index, pd.DatetimeIndex):
        plt.plot(observed_data.index, observed_data[value_col],
                linewidth=3, color='darkred', label='관측')
    else:
        plt.plot(observed_data[date_col], observed_data[value_col],
                linewidth=3, color='darkred', label='관측')

    # 예측값
    if isinstance(predicted_data.index, pd.DatetimeIndex):
        plt.plot(predicted_data.index, predicted_data[pred_col],
                linewidth=3, color='coral', label='예측', zorder=10)

        # 신뢰구간
        if ci_lower and ci_upper:
            plt.fill_between(predicted_data.index,
                           predicted_data[ci_lower],
                           predicted_data[ci_upper],
                           color='lightgray', alpha=0.65)
    else:
        plt.plot(predicted_data[date_col], predicted_data[pred_col],
                linewidth=3, color='coral', label='예측', zorder=10)

        if ci_lower and ci_upper:
            plt.fill_between(predicted_data[date_col],
                           predicted_data[ci_lower],
                           predicted_data[ci_upper],
                           color='lightgray', alpha=0.65)

    plt.title(title, loc='left', fontsize=20, fontweight='bold', pad=20)
    plt.xlabel('날짜(월)', fontsize=15, labelpad=15)
    plt.ylabel('공실률(%)', fontsize=15, labelpad=15)

    # 스타일 설정
    ax = plt.gca()
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(axis='y', color='black', alpha=0.4)
    plt.ylim(10, 40)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_feature_importance(feature_names, importances, top_n=None,
                            figsize=(6, 12), dpi=300,
                            title='Feature Importance'):
    """
    특성 중요도를 시각화합니다.

    Parameters:
    -----------
    feature_names : list
        특성 이름 리스트
    importances : array-like
        특성 중요도 값
    top_n : int
        상위 몇 개만 표시할지 (None이면 전체)
    figsize : tuple
        그래프 크기
    dpi : int
        해상도
    title : str
        그래프 제목
    """
    # 데이터프레임 생성
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    })
    feature_importance = feature_importance.sort_values('importance', ascending=False)

    if top_n:
        feature_importance = feature_importance.head(top_n)

    # 시각화
    plt.figure(figsize=figsize, dpi=dpi)
    bars = plt.barh(feature_importance['feature'],
                   feature_importance['importance'],
                   color='indianred')
    plt.xlabel('Importance')
    plt.title(title)
    plt.gca().invert_yaxis()

    # 스타일 설정
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.grid(False)

    # 값 표시
    for bar in bars:
        plt.text(bar.get_width() + 0.0003,
                bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():.2f}',
                va='center')

    plt.tight_layout()
    plt.show()


def plot_spatial_data(gdf, boundary_gdf=None, column=None,
                     figsize=(10, 10), title='공간 데이터 시각화',
                     cmap='coolwarm', legend=True):
    """
    공간 데이터를 시각화합니다.

    Parameters:
    -----------
    gdf : geopandas.GeoDataFrame
        시각화할 공간 데이터
    boundary_gdf : geopandas.GeoDataFrame
        경계 데이터 (optional)
    column : str
        시각화할 컬럼명 (None이면 단순 표시)
    figsize : tuple
        그래프 크기
    title : str
        그래프 제목
    cmap : str
        컬러맵
    legend : bool
        범례 표시 여부
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.grid(True)

    # 경계 표시
    if boundary_gdf is not None:
        boundary_gdf.plot(ax=ax, facecolor='none', edgecolor='gray',
                         linewidth=0.3, linestyle='--')

    # 데이터 표시
    if column:
        gdf.plot(ax=ax, column=column, cmap=cmap, legend=legend)
    else:
        gdf.plot(ax=ax, color='blue', alpha=0.5)

    plt.title(title, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
