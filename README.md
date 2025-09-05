# Brave Pink - Hero Green Filter WebApp 🎨

Aplikasi **Streamlit** sederhana untuk menerapkan filter pink dan hijau khusus pada gambar. Dibuat dengan semangat **perlawanan** menggunakan Python, Pillow, dan Streamlit.

-----

## 🚀 Fitur

  * Unggah gambar apa pun (JPG/PNG).
  * Terapkan efek **duotone(pink & green)** dengan warna kustom di sidebar.
  * Pratinjau dan unduh gambar yang telah diproses.
  * Antarmuka simpel.

-----

## 📂 Struktur Proyek

```
.
├── app.py              # Aplikasi utama Streamlit
├── requirements.txt    # Daftar dependensi
└── README.md           # Dokumentasi proyek
└── brave_pink_low.jpg  # Cover gambar
```

-----

## 🔧 Instalasi

1.  **Clone repositori:**

    ```bash
    git clone https://github.com/muhmuslimabdulj/brave-pink-filter-webapp.git
    cd brave-pink-filter-webapp
    ```

2.  **Buat virtual environment (direkomendasikan):**

    ```bash
    python -m venv venv
    # Aktifkan di Linux/Mac
    source venv/bin/activate
    # Aktifkan di Windows
    venv\Scripts\activate
    ```

3.  **Instal dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

-----

## ▶️ Cara Penggunaan

Jalankan aplikasi dengan perintah:

```bash
streamlit run app.py
```

Setelah itu, buka browser dan akses **[http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)**.

-----

## 📦 Dependensi

Aplikasi ini memerlukan pustaka berikut, detail semuanya tercantum dalam `requirements.txt`:

  * `streamlit`
  * `pillow`
  * `numpy`
  * `opencv-python`
