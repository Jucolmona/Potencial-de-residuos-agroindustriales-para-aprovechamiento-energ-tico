import streamlit as st

def encabezado_dashboard():
    col1, col2, col3 = st.columns(3, vertical_alignment='top')

    with col1:
        st.image("/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/image-1.png", width=300)

    with col2:
        st.header('Potencial de residuos agroindustriales para aprovechamiento energético')

    with col3:
        st.image("/workspaces/Potencial-de-residuos-agroindustriales-para-aprovechamiento-energ-tico/images/image-2.png", width=300)
        
def tabs_dashboard():
    tabs = st.tabs(['Contexto Nacional', 'Determinación de la capacidad calorífica',
              'Plantas de generación', 'Análisis y resultados', 'Locaciones para implementación'])
    return tabs

def tab_markdown(tab, path:str):
    with tab:
        with open(path, 'r') as file:
            markdown_content = file.read()
        st.markdown(markdown_content)

    