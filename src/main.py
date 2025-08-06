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
    plantas_data_frame = cargar_datos('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/dataSets/plantas.csv')
    potencial_energetico_data_frame = cargar_datos('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/dataSets/potencial energético.csv')
    potencial_calculado_df = cargar_datos('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/dataSets/potencial_energetico_calculado.csv')

    with tabs[0]:
        
        main = st.container()
        data_frames_container = st.container()
        with main:

            st.markdown("## Producción por grupo de cultivo")
            st.image('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/grafico_produccion_grupo_cultivo.png')

            st.markdown("## Distribución de producción según diferentes categorias")
            cols = st.columns(3, vertical_alignment='bottom')
            with cols[0]:
                st.image('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/grafico_distribucion_otros_permanentes.png',
                        width=400)
            with cols[1]:
                st.image('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/grafico_distribucion_tropicales_tradicionales.png',
                        width=450)
            with cols[2]:
                st.image('/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/grafico_distribucion_tuberculos_platanos.png',
                        width=370)
                
            st.markdown("## Producción por cultivo")
            st.image("/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/grafico_produccion_cultivo.png")

        with data_frames_container:
            st.markdown("## Data Frames usados")
            st.markdown("- ### Data Frame cultivos")
            st.write(cultivos_data_frame)
            st.markdown("- ### Data Frame plantas energeticas")
            st.write(plantas_data_frame)
            st.markdown("- ### Data frame potencial energético")
            st.write(potencial_energetico_data_frame)

    with tabs[2]:
        st.markdown("## Potencial energético calculado")
        st.write(potencial_calculado_df)

        datos = dsb.datos_calculo_PE(potencial_calculado_df)
        st.write(datos)
        plots.graficar_PE(datos[0], datos[1], datos[2], datos[3], datos[4])

    with tabs[3]:
        columnas_2 = st.columns(2)
        with columnas_2[0]:
            filtrado = dsb.datos_regresion(cultivos_data_frame)

        regresion_lineal = ml.entrenar_modelo(filtrado)
        dsb.resultados_regresion(regresion_lineal)
        grafica_regresion = plots.graficar_regresion(regresion_lineal[4],
                                                     regresion_lineal[5],
                                                     regresion_lineal[2],
                                                     regresion_lineal[3])
        
        with columnas_2[1]:
            dsb.graficar_dashboard(grafica_regresion)
        #st.write(cultivos_data_frame)

    with tabs[4]:
        columnas = st.columns(2)

        with columnas[0]:
            filtrado = dsb.datos_clustering(cultivos_data_frame)

        data_frame_filtrado = filtrado[0]
        st.write(filtrado[1])
        modelo_kmeans = ml.entrenar_kmeans(data_frame_filtrado)
        grafica = plots.graficar_kmeans(modelo_kmeans[0],
                                        modelo_kmeans[3],
                                        filtrado[1],
                                        n_clusters=filtrado[3])
        
        with columnas[1]:
            dsb.graficar_dashboard(grafica)
        