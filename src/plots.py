from typing import Tuple, List
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def graficar_regresion(y_test, y_pred, mse, r2):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Real vs Predicho
    ax[0].scatter(y_test, y_pred, alpha=0.6)
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax[0].plot(lims, lims, 'r--', lw=1.5)
    ax[0].set_xlabel('Real')
    ax[0].set_ylabel('Predicho')
    ax[0].set_title(f'Real vs Predicho\nMSE={mse:.2f} | R²={r2:.3f}')

    # 2. Residuos
    residuos = y_test - y_pred
    ax[1].scatter(y_pred, residuos, alpha=0.6)
    ax[1].axhline(0, color='r', ls='--')
    ax[1].set_xlabel('Predicho')
    ax[1].set_ylabel('Residuos')
    ax[1].set_title('Residuos vs Predicho')

    plt.tight_layout()
    return fig

def graficar_kmeans(df: pd.DataFrame,
                    centroids,
                    features: List[str] = None,
                    n_clusters: int = 3,
                    plot_3d: bool = False,
                    ):
    try:
        fig = plt.figure(figsize=(10, 6))
        if plot_3d and len(features) >= 3:
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(df[features[0]], df[features[1]], df[features[2]],
                    c=df['Cluster'], cmap='viridis', alpha=0.6)
            ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2],
                    s=200, c='red', marker='X', label='Centroides')
            ax.set_xlabel(features[0]); ax.set_ylabel(features[1]); ax.set_zlabel(features[2])
            ax.set_title(f'K-means 3D ({n_clusters} clusters)')
        else:
            ax = fig.add_subplot(111)
            ax.scatter(df[features[0]], df[features[1]],
                    c=df['Cluster'], cmap='viridis', alpha=0.6)
            ax.scatter(centroids[:, 0], centroids[:, 1],
                    s=200, c='red', marker='X', label='Centroides')
            ax.set_xlabel(features[0]); ax.set_ylabel(features[1])
            ax.set_title(f'K-means 2D ({n_clusters} clusters)')
            ax.legend()
        return fig
    except TypeError:
        st.write("Cantidad de caracteristicas no son suficiente para generar el gráfico")

def graficar_PE(df:pd.DataFrame, subproducto, departamento, periodo, cultivo):
    if not df.empty:
        # Agrupar por municipio para que no haya duplicados en la misma combinación
        plot_df = df.groupby("MUNICIPIO")[subproducto].sum().reset_index()

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(plot_df["MUNICIPIO"], plot_df[subproducto], color="skyblue")
        ax.set_xlabel("Municipio")
        ax.set_ylabel(subproducto)
        ax.set_title(f"{subproducto} – {departamento} – {periodo} – {cultivo}")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)
    else:
        st.warning("No hay datos para la combinación seleccionada.")

