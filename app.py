import cv2
import numpy as np
from PIL import Image
import streamlit as st
import io

# Custom CSS
st.set_page_config(page_title="Brave Pink-Hero Green", page_icon="🌸", layout="centered")
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
    <style>
    .custom-title {
        font-family: 'Bungee', sans-serif;
        font-size: clamp(1.5rem, 5vw, 2.5rem); 
        font-weight: bold;
        margin-bottom: 0.8rem;
    }
    .stDownloadButton button {
        background-color: #d63384;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
    }
    .stDownloadButton button:hover {
        background-color: #a61e66;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown(
    """
    <div style='text-align: center;'>
        <span class='custom-title' style='color:#d63384;'>Brave Pink</span>
        <span class='custom-title' style='color:#eaeaea;'> - </span>
        <span class='custom-title' style='color:#228B22;'>Hero Green</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Image Cover
col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image("brave_pink_low.jpg", width=400)

st.markdown("<p style='text-align:center; color:#6c757d;'>Satu Suara, Suara Perlawanan!</p>", unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    st.header("🎨 Settingan Filter")
    color_dark = st.color_picker("Settingan Warna Hijau", "#006400")   # Default hijau gelap
    color_light = st.color_picker("Settingan Warna Pink", "#FF69B4") # Default pink

    st.markdown("---")
    st.write("💡 **Tips:** Upload gambar berwarna terang agar efek filternya lebih terlihat.")

# Upload Gambar
uploaded_file = st.file_uploader("📤 Upload Gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    pil_img = Image.open(uploaded_file).convert("RGB")
    img = np.array(pil_img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    norm = gray / 255.0

    # Konversi warna hex ke BGR
    def hex_to_bgr(hex_color):
        h = hex_color.lstrip("#")
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return np.array(rgb[::-1])  # balik RGB -> BGR

    color_dark_bgr = hex_to_bgr(color_dark)
    color_light_bgr = hex_to_bgr(color_light)

    duotone_img = np.zeros_like(img, dtype=np.uint8)

    for i in range(3):
        duotone_img[:, :, i] = (
            color_dark_bgr[i] * (1 - norm) + color_light_bgr[i] * norm
        ).astype(np.uint8)

    duotone_rgb = cv2.cvtColor(duotone_img, cv2.COLOR_BGR2RGB)

    # Preview
    st.subheader("✨ Preview Hasil")
    col1, col2 = st.columns(2)
    with col1:
        st.image(pil_img, caption="Original", width="stretch")
    with col2:
        st.image(duotone_rgb, caption="Brave Pink-Hero Green", width="stretch")

    # Simpan untuk download
    result_pil = Image.fromarray(duotone_rgb)
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="⬇️ Download Hasil",
        data=byte_im,
        file_name="brave_pink.png",
        mime="image/png"
    )

# Footer: Privacy Policy & Credit
st.markdown("---", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align:center; font-size: 0.85rem; color: #6c757d;'>
        📢 <b>Privacy Notice:</b> Gambar yang kamu upload <b>tidak</b> disimpan di server.
        Semua proses dilakukan secara lokal untuk menjaga privasi.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align:center; font-size: 0.8rem; margin-top: 10px; color: #6c757d;'>
        Developed with Rebel by 
        <a href="https://www.instagram.com/malakais_1949/" target="_blank" style="color:#d63384; text-decoration:none;">
            @malakais_1949
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
