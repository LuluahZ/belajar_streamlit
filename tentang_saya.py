import streamlit as st
import pandas as pd
import numpy as np

def tampilkan_tentang_saya():
    st.header("Tentang Saya")
    st.subheader("Lu'Lu'Ah Zakiyah")
    st.write("Saya adalah data scientist dengan pengalaman di analitik data. Saya merupakan lulusan dari Institut Teknologi Hrapan Bangsa jurusan Sistem Informasi. " \
    "Saya memiliki pengalaman " \
    "sebagai Analis Sistem Informasi, dengan keterlibatan langsung dalam menganalisis sentimen terhadap kebijakan " \
    "pemerintah yang terkait dengan upaya pemulihan ekonomi selama pandemi.")

df = pd.DataFrame(
    {
        "Pendidikan": ["Institut Teknologi Harapan Bangsa", "MA MT Asih Putera", "SMPIT Sithrah Insani"],
        "Tahun lulus": [2023, 2018, 2015],
    }
)

config = {
    "Pendidikan": st.column_config.TextColumn("Pendidikan"),
    "Tahun Lulus": st.column_config.NumberColumn("Tahun lulus"),
}

st.dataframe(df, column_config=config)
st.write("Skills & Tools")
left, middle, right = st.columns(3, border=True)

left.markdown("Python")
middle.markdown("HTML")
right.markdown("Data Science")

left, middle = st.columns(2, border=True)

left.markdown("SQL")
middle.markdown("Tableau")

st.image("Lu'Lu'Ah Zakiyah.jpg")