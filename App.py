import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Eco3D", layout="wide")
st.title("🌱 Dashboard Estratégico - Eco3D Innovations")

# URLs de tus archivos desde GitHub (en formato RAW)
segmentacion_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/segmentacion_comercial.xlsx"
competidores_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/competidores.xlsx"
barreras_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/barreras_entrada.xlsx"
proyecciones_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/proyecciones_mercado.xlsx"
crecimiento_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/crecimiento_mercado_3D.xlsx"

# Cargar datos
@st.cache_data
def cargar_datos():
    segmentacion = pd.read_excel(segmentacion_url)
    competidores = pd.read_excel(competidores_url)
    barreras = pd.read_excel(barreras_url)
    proyecciones = pd.read_excel(proyecciones_url)
    crecimiento = pd.read_excel(crecimiento_url)
    return segmentacion, competidores, barreras, proyecciones, crecimiento

segmentacion, competidores, barreras, proyecciones, crecimiento = cargar_datos()

# Sección de segmentación comercial
st.header("🏬 Segmentación Comercial")
cadena = st.selectbox("Selecciona una cadena comercial:", segmentacion["Cadena Comercial"].unique())
st.dataframe(segmentacion[segmentacion["Cadena Comercial"] == cadena])

# Sección de competidores
st.header("🏭 Competidores")
st.dataframe(competidores)

# Sección de barreras de entrada
st.header("🚧 Barreras de Entrada")
st.dataframe(barreras)

# Sección de proyecciones de mercado (con gráfico)
st.header("📈 Proyecciones del Mercado")
st.dataframe(proyecciones)

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Construcción 3D (USD millones)"], marker="o", label="Construcción 3D EE.UU.")
ax1.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Global 3D (USD millones)"], marker="s", label="Mercado Global 3D")
ax1.set_title("Proyecciones del Mercado de Impresión 3D")
ax1.set_xlabel("Año")
ax1.set_ylabel("USD Millones")
ax1.legend()
st.pyplot(fig1)

# Sección adicional: crecimiento del mercado global 3D
st.header("📊 Crecimiento Global del Mercado 3D (2024–2032)")
st.dataframe(crecimiento)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(crecimiento["Año"], crecimiento["Tamaño Mercado Global 3D (USD mil millones)"], marker="o", color='green', label="Mercado Global 3D")
ax2.set_title("Crecimiento Proyectado del Mercado Global de Impresión 3D")
ax2.set_xlabel("Año")
ax2.set_ylabel("USD mil millones")
ax2.legend()
st.pyplot(fig2)
