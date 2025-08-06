import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def encabezado_dashboard():
    col1, col2, col3 = st.columns(3, vertical_alignment='top')

    with col1:
        st.image("/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/image-1.png", width=300)

    with col2:
        st.header('Potencial de residuos agroindustriales para aprovechamiento energético')

    with col3:
        st.image("/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/image-2.png", width=300)
        
def tabs_dashboard():
    tabs = st.tabs(['Contexto Nacional', 'Determinación de la capacidad calorífica', 'Potencial energético calculado',
              'Regresion lineal', 'Clustering K-means'])
    return tabs

def tab_markdown(tab, path:str):
    with tab:
        with open(path, 'r') as file:
            markdown_content = file.read()
        st.markdown(markdown_content)

def datos_regresion(df:pd.DataFrame):
    st.title("Regresión por municipio / cultivo")
    # 1. Filtro Departamento
    dep = st.selectbox("Departamento", sorted(df['DEPARTAMENTO'].unique()))

    # 2. Municipios disponibles para ese departamento
    municipios = sorted(df[df['DEPARTAMENTO'] == dep]['MUNICIPIO'].unique())
    mun = st.selectbox("Municipio", municipios)

    # 3. Cultivos disponibles para ese municipio
    cultivos = sorted(df[(df['DEPARTAMENTO'] == dep) & (df['MUNICIPIO'] == mun)]['CULTIVO'].unique())
    cultivo = st.selectbox("Cultivo", cultivos)

    data_frame_filtrado = df[(df['DEPARTAMENTO'] == dep) &
            (df['MUNICIPIO'] == mun) &
            (df['CULTIVO'] == cultivo)]
    
    
    st.write(data_frame_filtrado)
    return data_frame_filtrado

def resultados_regresion(resultados:tuple):
    st.metric("MSE", f"{resultados[2]:.2f}")
    st.metric("R²",  f"{resultados[3]:.3f}")
    
def datos_clustering(df:pd.DataFrame):
    st.title("Clustering K-means – Producción agrícola")

    # 1. Filtro Departamento
    departamento = sorted(df['DEPARTAMENTO'].unique())
    dep = st.selectbox("Departamento:", departamento)

    # 2. Municipios del departamento
    municipios = sorted(df[df['DEPARTAMENTO'] == dep]['MUNICIPIO'].unique())
    mun = st.selectbox("Municipio:", municipios)

    # 3. Cultivos disponibles para ese municipio
    cultivos = sorted(df[(df['DEPARTAMENTO'] == dep) & (df['MUNICIPIO'] == mun)]['CULTIVO'].unique())
    cultivo = st.selectbox("Cultivo:", cultivos)

    # 4. Número de clusters
    k = st.slider("Número de clusters (K)", 2, 10, 3)

    # 5. Tipo de gráfica
    plot_3d = st.checkbox("Gráfica 3D (requiere 3+ variables)")

    # Características a usar
    st.write("Definir caracteristicas para el modelo")
    char1 = st.checkbox('AREA SEMBRADA (ha)')
    char2 = st.checkbox('PRODUCCION (t)')
    char3 = st.checkbox('RENDIMIENTO (t/ha)')

    if char1 == True and char2 == True: 
        features = ['AREA SEMBRADA (ha)', 'PRODUCCION (t)']
    elif char1 == True and char3 == True:
        features = ['AREA SEMBRADA (ha)', 'RENDIMIENTO (t/ha)']
    elif char2 == True and char3 == True:
        features = ['PRODUCCION (t)', 'RENDIMIENTO (t/ha)']
    elif char1 == True and char2 == True and char3 == True:
        features = ['AREA SEMBRADA (ha)', 'PRODUCCION (t)', 'RENDIMIENTO (t/ha)']
    else:
        st.write('Tiene que elegir al menos dos caracteristicas para el modelo')
        features = None

    # Filtrar
    sub_df = df[(df['DEPARTAMENTO'] == dep) &
                (df['MUNICIPIO'] == mun) &
                (df['CULTIVO'] == cultivo)]
    
    return sub_df, features, plot_3d, k

def graficar_dashboard(grafica):
    st.pyplot(grafica)

def datos_calculo_PE(df:pd.DataFrame):
    st.title("Gráfico dinámico de subproductos por filtro")

    # 1. Departamento
    departamento = st.selectbox("Departamento", sorted(df["DEPARTAMENTO"].unique()))

    # 2. Periodos que existen en ese departamento
    periodos = sorted(df[df["DEPARTAMENTO"] == departamento]["PERIODO"].unique())
    periodo  = st.selectbox("Periodo", periodos)

    # 3. Cultivos que existen en (departamento, periodo)
    cultivos = sorted(df[(df["DEPARTAMENTO"] == departamento) & (df["PERIODO"] == periodo)]["CULTIVO"].unique())
    cultivo = st.selectbox("Cultivo", cultivos)

    # 4. Subproducto (sin restricción extra; puede ser cualquiera)
    subproducto = st.selectbox(
        "Subproducto (eje Y)", ["PRODUCCIÓN (t)", "RENDIMIENTO (t/ha)", "ÁREA SEMBRADA (ha)"]
    )

    # 5. DataFrame filtrado final
    sub_df = df[
        (df["DEPARTAMENTO"] == departamento)
        & (df["PERIODO"] == periodo)
        & (df["CULTIVO"] == cultivo)
    ]
    return sub_df, subproducto, departamento, periodo, cultivo
    
   