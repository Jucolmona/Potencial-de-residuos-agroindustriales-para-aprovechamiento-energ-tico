from typing import Tuple, List
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def entrenar_modelo(df: pd.DataFrame,
                    caracteristicas_categoricas: list = None,
                    caracteristicas_numericas: list = None,
                    target: str = 'PRODUCCION (t)',
                    test_size: float = 0.2,
                    random_state: int = 42
                    ):
    if df.empty:
        raise ValueError("El DataFrame está vacío, no se puede entrenar.")
    
    # columnas por defecto
    if caracteristicas_categoricas is None:
        caracteristicas_categoricas = ['DEPARTAMENTO', 'MUNICIPIO', 'CICLO DE CULTIVO']
    if caracteristicas_numericas is None:
        caracteristicas_numericas = ['AREA SEMBRADA (ha)']
    
    X = df[caracteristicas_categoricas + caracteristicas_numericas]
    y = df[target]
    
    # Codificar categóricas
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    X_cat = encoder.fit_transform(X[caracteristicas_categoricas])
    
    # Concatenar con numéricas
    X_num = X[caracteristicas_numericas].values
    X_processed = np.hstack([X_cat, X_num])
    
    # Split / train
    X_tr, X_te, y_tr, y_te = train_test_split(
        X_processed, y, test_size=test_size, random_state=random_state
    )
    model = LinearRegression()
    model.fit(X_tr, y_tr)
    
    # Métricas
    y_pred = model.predict(X_te)
    mse = mean_squared_error(y_te, y_pred)
    r2  = r2_score(y_te, y_pred)
    
    return model, encoder, mse, r2, y_te, y_pred

def entrenar_kmeans(df: pd.DataFrame,
                    features: List[str] = None,
                    n_clusters: int = 3,
                    random_state: int = 42
                    ):
    if df.empty:
        raise ValueError("DataFrame vacío")

    features = features or ['AREA SEMBRADA (ha)', 'PRODUCCION (t)', 'RENDIMIENTO (t/ha)']
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df = df.copy()
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    centroids = scaler.inverse_transform(kmeans.cluster_centers_)

    return df, scaler, kmeans, centroids