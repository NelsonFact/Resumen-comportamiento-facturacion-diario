import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración profesional
st.set_page_config(page_title="Dashboard Clínica 2026", layout="wide")

st.title("🏥 Reporte Gerencial - Movimiento de la Clínica")
st.markdown("---")

@st.cache_data
def load_data():
    # Cargamos los archivos con los nombres simplificados
    resumen = pd.read_csv('resumen.csv')
    egresos = pd.read_csv('egresos.csv')
    return resumen, egresos

try:
    df_res, df_egr = load_data()
    
    # --- FILA 1: MÉTRICAS PRINCIPALES ---
    col1, col2, col3 = st.columns(3)
    with col1:
        total_fact = df_res['valor_total'].sum()
        st.metric("Facturación Total", f"${total_fact:,.0f}")
    with col2:
        st.metric("Total Egresos", f"{len(df_egr)} Pacientes")
    with col3:
        sedes = df_res['SEDE'].nunique()
        st.metric("Sedes Activas", sedes)

    st.markdown("---")

    # --- FILA 2: GRÁFICOS INTERACTIVOS ---
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Facturación por Sede")
        fig_pie = px.pie(df_res, names='SEDE', values='valor_total', hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with c2:
        st.subheader("Facturación por Servicio")
        fig_bar = px.bar(df_res.groupby('servicio')['valor_total'].sum().reset_index(), 
                         x='servicio', y='valor_total', color='servicio')
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- TABLA DE DATOS ---
    with st.expander("Ver detalle de datos"):
        st.write(df_res)

except Exception as e:
    st.error(f"Error de configuración: {e}")
    st.info("Asegúrate de que los archivos en GitHub se llamen 'resumen.csv' y 'egresos.csv'")