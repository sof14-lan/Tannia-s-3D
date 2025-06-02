import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración general
st.set_page_config(page_title="Dashboard Eco3D", layout="wide")
st.title("🌱 Dashboard Estratégico - Eco3D Innovations")

# --- RUTAS DE ARCHIVOS DESDE TU REPO ---
BASE_URL = "https://raw.githubusercontent.com/sof14-lan/Eco-3d-Innovations/main/"
segmentacion_url = BASE_URL + "segmentacion_comercial.xlsx"
competidores_url = BASE_URL + "competidores.xlsx"
barreras_url = BASE_URL + "barreras_entrada.xlsx"
proyecciones_url = BASE_URL + "proyecciones_mercado.xlsx"

# --- CARGA DE DATOS ---
@st.cache_data
def cargar_datos():
    segmentacion = pd.read_excel(segmentacion_url)
    competidores = pd.read_excel(competidores_url)
    barreras = pd.read_excel(barreras_url)
    proyecciones = pd.read_excel(proyecciones_url)
    return segmentacion, competidores, barreras, proyecciones

segmentacion, competidores, barreras, proyecciones = cargar_datos()

# --- SECCIÓN: Segmentación Comercial ---
st.header("🏬 Segmentación Comercial")
cadena = st.selectbox("Selecciona una cadena comercial:", segmentacion["Cadena Comercial"].unique())
st.dataframe(segmentacion[segmentacion["Cadena Comercial"] == cadena])

# --- SECCIÓN: Competidores ---
st.header("🏭 Competidores")
st.dataframe(competidores)

# --- SECCIÓN: Barreras de Entrada ---
st.header("🚧 Barreras de Entrada")
st.dataframe(barreras)

# --- SECCIÓN: Proyecciones del Mercado ---
st.header("📈 Proyecciones del Mercado")
st.dataframe(proyecciones)

# --- Gráfico de Proyecciones ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Construcción 3D (USD millones)"],
        marker="o", label="Construcción 3D EE.UU.")
ax.plot(proyecciones["Año"], proyecciones["Tamaño Mercado Global 3D (USD millones)"],
        marker="s", label="Mercado Global 3D")
ax.set_title("Proyecciones del Mercado de Impresión 3D")
ax.set_xlabel("Año")
ax.set_ylabel("USD Millones")
ax.legend()
st.pyplot(fig)
