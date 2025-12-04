import streamlit as st
from PIL import Image
import os

st.title("Home")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### Matrix Transformations Web App")
st.write("Aplikasi ini memperlihatkan transformasi matriks (translation, scaling, rotation, shear, reflection) dan filter konvolusi (blur & sharpen).")
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])
with col1:
    st.markdown("## How it works")
    txt = ("- Transformasi geometris dibuat dengan matriks homogen 3x3 dan diterapkan ke koordinat piksel (backward mapping).\n"
           "- Konvolusi untuk blur dan sharpen diimplementasikan manual dengan kernel.\n"
           "- Upload gambar di halaman *Image Tools*, atur parameter di sidebar, dan lihat hasilnya.")
    st.write(txt)
    st.markdown("### Quick tips")
    st.write("- Gunakan gambar berukuran sedang agar proses cepat.")
    st.write("- Untuk hasil halus pada transformasi, pilih bilinear interpolation (opsional).")
with col2:
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=260)

st.markdown("---")
st.markdown("### Visual examples")
imgs = []
if os.path.exists("assets/example_before.jpg") and os.path.exists("assets/example_after.jpg"):
    imgs = [Image.open("assets/example_before.jpg"), Image.open("assets/example_after.jpg")]
if imgs:
    st.image(imgs, caption=["Before","After"], use_column_width=True)

   