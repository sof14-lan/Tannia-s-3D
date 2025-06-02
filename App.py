import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Eco3D", layout="wide")
st.title("🌱 Dashboard Estratégico - Eco3D Innovations")

# URLs de tus archivos reales desde GitHub
segmentacion_url = "https://github.com/sof14-lan/Tannia-s-3D/raw/refs/heads/main/segmentacion_comercial.xlsx"
competidores_url = "https://github.com/sof14-lan/Tannia-s-3D/raw/refs/heads/main/competidores.xlsx"
barreras_url = "https://github.com/sof14-lan/Tannia-s-3D/raw/refs/heads/main/barreras_entrada.xlsx"
proyecciones_url = "https://github.com/sof14-lan/Tannia-s-3D/raw/refs/heads/main/proyecciones_mercado.xlsx"

@st.cache_data
def cargar_datos():
    segmentacion = pd.read_excel(segmentacion_url)
