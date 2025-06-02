import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Eco3D", layout="wide")
st.title("🌱 Dashboard Estratégico - Eco3D Innovations")

# ✅ Enlaces RAW CORRECTOS desde GitHub
segmentacion_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/segmentacion_comercial.xlsx"
competidores_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/competidores.xlsx"
barreras_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/barreras_entrada.xlsx"
proyecciones_url = "https://raw.githubusercontent.com/sof14-lan/Tannia-s-3D/main/proyecciones_mercado.xlsx"

# Cargar datos
@st.cache_data
def cargar_datos():
    segmentacion = pd.read_excel(segmentacion_url)
    competidores = pd.read_excel(competidores_url)
    barreras = pd.read_excel(barreras_url)
    proyecciones = pd.read_excel(proyecciones_url)
    return segmentacion, competidores, barreras, proyecciones

segmentacion, competidores, barreras, proyecciones = cargar_datos()

# Mostrar sección de segmentación comercial
st.header("🏬 Segmentación Comercial")
cadena = st.selectbox("Selecciona una cadena comercial:", segmentacion["Cadena Comercial"].unique())
st.dataframe(segmentacion[segmentacion["Cadena Comercial"] == cadena])

# Mostrar sección de competidores
st.header("🏭 Competidores")
st.dataframe(competidores)

# Mostrar sección de barreras de entrada
st.header("🚧 Barreras de Entrada")
st.dataframe(barreras)

# Mostrar sección de proyecciones del mercado
st.header("📈 Proyecciones del Mercado")
st.dataframe(proyecciones)

# Gráfico de proyecciones
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Construcción 3D (USD millones)"], marker="o", label="Construcción 3D EE.UU.")
ax.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Global 3D (USD millones)"], marker="s", label="Mercado Global 3D")
ax.set_title("Proyecciones del Mercado de Impresión 3D")
ax.set_xlabel("Año")
ax.set_ylabel("USD Millones")
ax.legend()
st.pyplot(fig)
