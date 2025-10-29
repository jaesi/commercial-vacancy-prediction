"""
Modeling module
모델링 모듈
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


def split_data(X, y, test_size=0.15, random_state=42):
    """
    데이터를 학습/테스트 세트로 분할합니다.

    Parameters:
    -----------
    X : pandas.DataFrame
        특성 데이터
    y : pandas.Series
        타겟 데이터
    test_size : float
        테스트 세트 비율
    random_state : int
        랜덤 시드

    Returns:
    --------
    tuple : X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_random_forest(X_train, y_train, params=None, random_search=False):
    """
    Random Forest 모델을 학습합니다.

    Parameters:
    -----------
    X_train : pandas.DataFrame
        학습 특성 데이터
    y_train : pandas.Series
        학습 타겟 데이터
    params : dict
        모델 파라미터
    random_search : bool
        RandomizedSearchCV 사용 여부

    Returns:
    --------
    model : 학습된 모델
    """
    if random_search and params:
        rf = RandomForestRegressor()
        rf_random = RandomizedSearchCV(
            estimator=rf,
            param_distributions=params,
            n_iter=100,
            cv=5,
            verbose=2,
            random_state=42,
            n_jobs=-1
        )
        rf_random.fit(X_train, y_train)
        print('Best Parameters:', rf_random.best_params_)
        return rf_random.best_estimator_
    else:
        if params is None:
            params = {'random_state': 42}
        rf = RandomForestRegressor(**params)
        rf.fit(X_train, y_train)
        return rf


def train_gradient_boosting(X_train, y_train, params=None):
    """
    Gradient Boosting 모델을 학습합니다.

    Parameters:
    -----------
    X_train : pandas.DataFrame
        학습 특성 데이터
    y_train : pandas.Series
        학습 타겟 데이터
    params : dict
        모델 파라미터

    Returns:
    --------
    model : 학습된 모델
    """
    if params is None:
        params = {'random_state': 42}
    gbr = GradientBoostingRegressor(**params)
    gbr.fit(X_train, y_train)
    return gbr


def evaluate_model(model, X_test, y_test):
    """
    모델을 평가합니다.

    Parameters:
    -----------
    model : sklearn model
        평가할 모델
    X_test : pandas.DataFrame
        테스트 특성 데이터
    y_test : pandas.Series
        테스트 타겟 데이터

    Returns:
    --------
    dict : 평가 지표 (MSE, RMSE, R2)
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    results = {
        'MSE': mse,
        'RMSE': rmse,
        'R2': r2
    }

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R^2 Score: {r2:.4f}")

    return results


def get_feature_importance(model, feature_names):
    """
    특성 중요도를 반환합니다.

    Parameters:
    -----------
    model : sklearn model
        학습된 모델 (feature_importances_ 속성 필요)
    feature_names : list
        특성 이름 리스트

    Returns:
    --------
    pandas.DataFrame : 특성 중요도 데이터프레임
    """
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    })
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    return feature_importance


def train_arima(data, order=(10, 1, 5), steps=19):
    """
    ARIMA 모델을 학습하고 예측합니다.

    Parameters:
    -----------
    data : pandas.Series
        시계열 데이터
    order : tuple
        ARIMA 차수 (p, d, q)
    steps : int
        예측할 기간 수

    Returns:
    --------
    tuple : (fitted_model, forecast_df)
    """
    model = ARIMA(data, order=order)
    fitted = model.fit()
    forecast = fitted.get_forecast(steps=steps)
    forecast_df = forecast.summary_frame()
    return fitted, forecast_df


def train_sarima(data, order=(10, 1, 5), seasonal_order=(1, 1, 1, 12), steps=19):
    """
    SARIMA 모델을 학습하고 예측합니다.

    Parameters:
    -----------
    data : pandas.Series
        시계열 데이터
    order : tuple
        ARIMA 차수 (p, d, q)
    seasonal_order : tuple
        계절성 차수 (P, D, Q, s)
    steps : int
        예측할 기간 수

    Returns:
    --------
    tuple : (fitted_model, forecast_df)
    """
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
    fitted = model.fit(disp=False)
    forecast = fitted.get_forecast(steps=steps)
    forecast_df = forecast.summary_frame()
    return fitted, forecast_df


# Random Forest 하이퍼파라미터 그리드
RF_PARAM_GRID = {
    'n_estimators': [5, 20, 50, 100],
    'max_features': ['auto', 'sqrt'],
    'max_depth': [int(x) for x in np.linspace(10, 120, num=12)],
    'min_samples_split': [2, 6, 10],
    'min_samples_leaf': [1, 3, 4],
    'bootstrap': [True, False]
}
