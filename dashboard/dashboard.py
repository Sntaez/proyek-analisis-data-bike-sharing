import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Memuat data dari file CSV
file_path = "../dashboard/main_data.csv"
df = pd.read_csv(file_path)

st.title("Dashboard Penyewaan Sepeda")

menu = st.sidebar.selectbox("Pilih Analisis", ["Ringkasan Data", "Tren Penyewaan", "Pengaruh Cuaca"])

# Menu ringkasan data
if menu == "Ringkasan Data":
    st.header("Ringkasan Data Penyewaan Sepeda")
    st.write(df.describe())

    # Distribusi Penyewaan Sepeda
    st.subheader("Distribusi Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.histplot(df["cnt"], bins=30, kde=True, ax=ax, color=sns.color_palette("viridis")[3])
    
    # Mengubah label sumbu X
    ax.set_xlabel("\nJumlah Penyewaan")
    ax.set_ylabel("Jumlah Hari\n")
    
    st.pyplot(fig)


# Menu tren penyewaan
elif menu == "Tren Penyewaan":
    st.header("Tren Penyewaan Sepeda")

    # Penyewaan per hari dalam seminggu
    st.subheader("Rata-rata Penyewaan Sepeda per Hari dalam Seminggu")
    day_names = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    day_trend = df.groupby("weekday")["cnt"].mean()
    fig, ax = plt.subplots()
    day_trend.plot(kind="bar", color="orange", ax=ax)

    ax.set_xticklabels(day_names, rotation=0)      
    ax.set_xlabel("\nHari")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda\n")
    
    st.pyplot(fig)


    # Penyewaan per bulan
    st.subheader("Rata-rata Penyewaan Sepeda per Bulan")
    month_trend = df.groupby("mnth")["cnt"].mean()
    month_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    fig, ax = plt.subplots()
    month_trend.plot(kind="bar", color="green", ax=ax)
    ax.set_xticklabels(month_names, rotation=0)
    ax.set_xlabel("\nBulan")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda\n")
    st.pyplot(fig)

    # Penyewaan per musim
    st.subheader("Rata-rata Penyewaan Sepeda per Musim")
    season_trend = df.groupby("season")["cnt"].mean()
    season_names = ["Semi", "Panas", "Gugur", "Dingin"]
    fig, ax = plt.subplots()
    season_trend.plot(kind="bar", colormap="cividis", ax=ax)
    ax.set_xticklabels(season_names, rotation=0)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda\n")
    st.pyplot(fig)

# Menu pengaruh cuaca
elif menu == "Pengaruh Cuaca":
    st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")

    # Penyewaan berdasarkan kondisi cuaca
    st.subheader("Rata-rata Penyewaan berdasarkan Kondisi Cuaca")
    weather_trend = df.groupby("weathersit")["cnt"].mean()
    weather_names = ["Cerah", "Berkabut & Berawan", "Salju/Hujan Ringan"]
    fig, ax = plt.subplots()
    weather_trend.plot(kind="bar", color="Gold", ax=ax)
    ax.set_xticklabels(weather_names, rotation=0)
    ax.set_xlabel("\nCuaca")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda\n")
    st.pyplot(fig)