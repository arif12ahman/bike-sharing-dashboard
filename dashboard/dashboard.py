import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    return pd.read_csv("final_data.csv")

data = load_data()

# Dashboard Title
st.title("Dashboard Analisis Data: Bike Sharing")

# Sidebar
st.sidebar.header("Filter Data")
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:",
    options=data["weathersit"].unique(),
    default=data["weathersit"].unique()
)

selected_weekday = st.sidebar.multiselect(
    "Pilih Hari:",
    options=data["hr"].unique(),
    default=data["hr"].unique()
)

# Filter data
filtered_data = data[
    (data["weathersit"].isin(selected_weather)) &
    (data["hr"].isin(selected_weekday))
]

# Display filtered data
st.subheader("Data yang Difilter")
st.dataframe(filtered_data)

# Visualization 1: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
weather_group = filtered_data.groupby("weathersit")["cnt_day"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x="weathersit", y="cnt_day", data=weather_group, palette="Set2", ax=ax1)
ax1.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig1)

# Visualization 2: Pola Penggunaan Sepeda Berdasarkan Hari
st.subheader("Pola Penggunaan Sepeda Berdasarkan Hari")
weekday_group = filtered_data.groupby("weekday")["cnt_hour"].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="weekday", y="cnt_hour", data=weekday_group, palette="Set1", ax=ax2)
ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Hari")
ax2.set_xlabel("Hari")
ax2.set_ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig2)

# Visualization 3: Pola Penggunaan Sepeda Berdasarkan Jam
st.subheader("Pola Penggunaan Sepeda Berdasarkan Jam")
hour_group = filtered_data.groupby("hr")["cnt_hour"].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(x="hr", y="cnt_hour", data=hour_group, marker="o", ax=ax3)
ax3.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax3.set_xlabel("Jam")
ax3.set_ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig3)
