import dashboard as dsb
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
        dsb.datos_regresion(cultivos_data_frame)
        #st.write(cultivos_data_frame)