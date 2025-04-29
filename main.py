import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":rocket:")
st.title("Portfolio Saya")
st.header("Data Scientist & Developer")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Tentang Saya", "Proyek", "Kontak"])

if page == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()
elif page == "Kontak":
    import kontak
    kontak.tampilkan_kontak()
elif page == "Proyek":
    import visualisasi
    visualisasi.tampilkan_visualisasi()