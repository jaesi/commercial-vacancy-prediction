"""
Configuration module for common settings
공통 설정 모듈
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

def setup_environment():
    """
    환경 설정을 초기화합니다.
    - 경고 메시지 숨기기
    - Matplotlib 한글 폰트 설정
    - Pandas 표시 옵션 설정
    """
    # 경고 메시지 숨기기
    warnings.filterwarnings('ignore')

    # Matplotlib 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

    # Pandas 옵션 설정
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', 300)

    print("환경 설정 완료: 한글 폰트 및 pandas 옵션 설정됨")


# 프랜차이즈 리스트
FRANCHISE_LIST = [
    '스타벅스', '이디야', '투썸플레이스', '커피빈', '할리스', '탐앤탐스',
    '빽다방', '엔제리너스', '파스쿠찌', '커피베이', '60계',
    '홍콩반점', '올리브영', '가마로강정', '가마치통닭', '강다짐',
    '걸작떡볶이치킨', '고릴라캠핑', '공차', '교촌치킨', '굽네치킨',
    '김가네', '노랑통닭', '노브랜드 버거', '다이소', '도미노',
    '롯데리아', '맘스터치', '메가엠지씨', '멕시카나', '버거킹'
]

# 날짜 범위 (2012.07 ~ 2024.05)
DATE_RANGE_START = '2012-07-01'
DATE_RANGE_END = '2024-05-01'
