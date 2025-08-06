import dashboard as dsb
import machineLearning as ml
import plots
import streamlit as st
import pandas as pd

def cargar_datos(path:str):
    data_frame = pd.read_csv(path)
    return data_frame

if __name__ == "__main__":
    dsb.encabezado_dashboard()

    tabs = dsb.tabs_dashboard()
    
    dsb.tab_markdown(tabs[1], '/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/markdowns/determinacion-1.md')

    cultivos_data_frame = cargar_datos('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/dataSets/cultivos_def.csv')

    with tabs[2]:
        filtrado = dsb.datos_regresion(cultivos_data_frame)
        regresion_lineal = ml.entrenar_modelo(filtrado)
        dsb.resultados_regresion(regresion_lineal)
        grafica_regresion = plots.graficar_regresion(regresion_lineal[4],
                                                     regresion_lineal[5],
                                                     regresion_lineal[2],
                                                     regresion_lineal[3])
        dsb.graficar_dashboard(grafica_regresion)
        #st.write(cultivos_data_frame)

    with tabs[3]:
        filtrado = dsb.datos_clustering(cultivos_data_frame)[0]
        modelo_kmeans = ml.entrenar_kmeans(filtrado)
        grafica = plots.graficar_kmeans(modelo_kmeans[0],
                                        modelo_kmeans[3],
                                        filtrado[1])
        