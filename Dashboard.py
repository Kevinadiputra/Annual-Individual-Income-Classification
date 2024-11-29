import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Data Sensus")
st.write("Analisis dan Visualisasi Data Sensus")



df = pd.read_csv('Dashboard/adult.csv')
# Tampilkan beberapa baris data
st.subheader("Pratinjau Data")
st.write(df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(df.describe())

# Visualisasi Distribusi Data
st.subheader("Visualisasi Distribusi Data")
numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

selected_column = st.selectbox("Pilih Kolom untuk Histogram", numeric_columns)
bins = st.slider("Jumlah Bin (Histogram)", min_value=5, max_value=50, value=10)

# Histogram
fig, ax = plt.subplots()
sns.histplot(df[selected_column], bins=bins, kde=True, ax=ax)
ax.set_title(f"Distribusi Kolom {selected_column}")
st.pyplot(fig)

# Heatmap Korelasi
st.subheader("Korelasi Antar Variabel")
corr = df.corr(numeric_only = True)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Filter Data
st.subheader("Filter Data")
categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
filter_column = st.selectbox("Pilih Kolom untuk Filter", categorical_columns)

unique_values = df[filter_column].unique()
selected_value = st.selectbox(f"Pilih Nilai dari {filter_column}", unique_values)

filtered_data = df[df[filter_column] == selected_value]
st.write(f"Data yang difilter berdasarkan {filter_column} = {selected_value}")
st.write(filtered_data)

# Bar Plot untuk Variabel Kategorikal
st.subheader("Visualisasi Variabel Kategorikal")
selected_categorical_column = st.selectbox("Pilih Kolom Kategorikal untuk Bar Plot", categorical_columns)

fig, ax = plt.subplots()
sns.countplot(y=df[selected_categorical_column], order=df[selected_categorical_column].value_counts().index, ax=ax)
ax.set_title(f"Distribusi {selected_categorical_column}")
st.pyplot(fig)

# Scatter Plot
st.subheader("Scatter Plot untuk Hubungan Antar Variabel")
x_axis = st.selectbox("Pilih Kolom X", numeric_columns)
y_axis = st.selectbox("Pilih Kolom Y", numeric_columns)

fig, ax = plt.subplots()
sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
ax.set_title(f"{x_axis} vs {y_axis}")
st.pyplot(fig)

# Insight
st.subheader("Insight Data")
st.write("1. Distribusi data dapat dilihat dari histogram dan bar chart.")
st.write("2. Korelasi antar variabel memberikan gambaran hubungan antar fitur.")
st.write("3. Scatter plot membantu memvisualisasikan hubungan antara dua variabel numerik.")