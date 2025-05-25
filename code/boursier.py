import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import requests

# 📌 Interface utilisateur avec Streamlit
st.title("📈 Surveillance Boursière : Marchés Français & Américains")
st.sidebar.header("Paramètres")
ticker = st.sidebar.text_input("Entrez un symbole boursier (ex: AAPL, TSLA, CAC40)", "AAPL")
periode = st.sidebar.selectbox("Période d'analyse", ["6mo", "1y", "5y", "max"], index=1)

# 📉 Récupération des données financières
st.sidebar.write("🔄 Chargement des données...")
data = yf.Ticker(ticker).history(period=periode)

# 📊 Calcul des Indicateurs Techniques
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()
short_ema = data['Close'].ewm(span=12, adjust=False).mean()
long_ema = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = short_ema - long_ema
data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

# 📈 Affichage des Graphiques
st.subheader(f"Analyse des tendances de {ticker}")
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(data.index, data['Close'], label="Cours de clôture", color="blue")
ax.plot(data.index, data['SMA_50'], label="SMA 50", linestyle="dashed", color="green")
ax.plot(data.index, data['SMA_200'], label="SMA 200", linestyle="dashed", color="red")
ax.set_title(f"Analyse Boursière de {ticker}")
ax.legend()
st.pyplot(fig)

# 📊 Affichage du MACD
st.subheader("Indicateurs MACD")
st.line_chart(data[['MACD', 'Signal_Line']])

st.success("✅ Analyse complétée avec succès !")
