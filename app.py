import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard Clínica 2026", layout="wide")
st.title("🏥 Reporte Gerencial - Movimiento de la Clínica")

# Esta función busca cualquier archivo que contenga la palabra 'resumen'
def find_file(name_part):
    for file in os.listdir('.'):
        if name_part in file.lower() and file.endswith('.csv'):
            return file
    return None

try:
    # Intentamos buscar el archivo automáticamente
    archivo_resumen = find_file('resumen')
    
    if archivo_resumen:
        df = pd.read_csv(archivo_resumen)
        st.success(f"✅ Cargado con éxito: {archivo_resumen}")
        
        # --- MÉTRICAS ---
        # Usamos nombres de columnas basados en tus archivos cargados
        col1, col2 = st.columns(2)
        with col1:
            # En tus datos la columna se llama 'valor_total'
            total = df['valor_total'].sum()
            st.metric("Facturación Total", f"${total:,.0f}")
        with col2:
            st.metric("Total Facturas", len(df))

        # --- GRÁFICO ---
        st.subheader("Análisis por Sede y Servicio")
        fig = px.bar(df, x='servicio', y='valor_total', color='SEDE', 
                     title="Facturación por Especialidad", barmode='group')
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.error("❌ No encontré ningún archivo que diga 'resumen' en el repositorio.")
        st.info("Archivos detectados: " + str(os.listdir('.')))

except Exception as e:
    st.error(f"Hubo un problema con los datos: {e}")
