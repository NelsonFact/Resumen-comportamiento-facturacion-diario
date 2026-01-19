import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Dashboard Clínica 2026", layout="wide")

st.title("🏥 Reporte Gerencial - Movimiento de la Clínica")

# Carga de datos usando los nombres reales de tus archivos
@st.cache_data
def load_data():
    # Cargamos la hoja de resumen que subiste
    df_res = pd.read_csv('Resumen comportamiento facturacion diario 2026 (1).xlsx - resumen.csv')
    return df_res

try:
    df = load_data()
    
    # KPIs rápidos
    col1, col2 = st.columns(2)
    with col1:
        total = df['valor_total'].sum()
        st.metric("Facturación Total", f"${total:,.0f}")
    with col2:
        num_facturas = len(df)
        st.metric("Total Facturas Emitidas", num_facturas)

    # Gráfico de barras por Servicio
    st.subheader("Distribución por Servicio")
    fig = px.bar(df, x='servicio', y='valor_total', color='SEDE', title="Facturación por Servicio y Sede")
    st.plotly_chart(fig, use_container_width=True)

    # Detalle de la tabla
    with st.expander("Ver base de datos completa"):
        st.write(df)

except Exception as e:
    st.error(f"Error al cargar datos: {e}")
    st.info("Asegúrate de subir el archivo CSV con el nombre exacto al repositorio.")