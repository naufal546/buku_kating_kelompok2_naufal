import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown(
    """<style>.centered-title {text-align: center;}</style>""",
    unsafe_allow_html=True,
)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# Create a menu for department navigation
def streamlit_menu():
    options = [
        "Kesekjenan",
        "Baleg",
        "Senator",
        "Departemen PSDA",
        "Departemen MIKFES",
        "Departemen Eksternal",
        "Departemen Internal",
        "Departemen SSD",
    ]
    icons = ["people-fill"] * len(options)
    
    selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

# Load images from URLs with error handling
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except requests.RequestException as e:
        st.error(f"Failed to fetch image from {url}, error: {e}")
    except Exception as e:
        st.error(f"Error loading image: {e}")
    return None

# Display images with corresponding data
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    for i, (url, data) in enumerate(zip(gambar_urls, data_list)):
        with st.spinner(f"Loading image {i + 1}/{len(gambar_urls)}"):
            img = load_image(url)
            if img:
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.image(img, use_column_width=True)
                st.write(f"Nama: {data['nama']}")
                st.write(f"NIM: {data['nim']}")
                st.write(f"Umur: {data['umur']}")
                st.write(f"Asal: {data['asal']}")
                st.write(f"Alamat: {data['alamat']}")
                st.write(f"Hobbi: {data['hobbi']}")
                st.write(f"Sosial Media: {data['sosmed']}")
                st.write(f"Kesan: {data['kesan']}")
                st.write(f"Pesan: {data['pesan']}")
                st.write(" ")

# Display section based on menu selection
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [
        {
            "nama": "Kakak A",
            "nim": "122450000",
            "umur": "18",
            "asal": "Bekasi",
            "alamat": "Gg. Sakum",
            "hobbi": "Main bola, belajar",
            "sosmed": "@i",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "Semangat terus kuliahnya kakak!!!"
        },
        {
            "nama": "Kakak B",
            "nim": "122450001",
            "umur": "19",
            "asal": "Jakarta",
            "alamat": "Jl. Merdeka",
            "hobbi": "Membaca, olahraga",
            "sosmed": "@b",
            "kesan": "Kakaknya sangat rajin dan membantu",
            "pesan": "Tetap semangat dan terus maju!"
        },
        {
            "nama": "Kakak C",
            "nim": "122450002",
            "umur": "20",
            "asal": "Bandung",
            "alamat": "Jl. Asia Afrika",
            "hobbi": "Menulis, berenang",
            "sosmed": "@c",
            "kesan": "Kakaknya hebat dan selalu memberi motivasi",
            "pesan": "Jangan menyerah kak!"
        },
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [
        {
            "nama": "Kakak D",
            "nim": "122450003",
            "umur": "21",
            "asal": "Yogyakarta",
            "alamat": "Jl. Malioboro",
            "hobbi": "Mendaki, fotografi",
            "sosmed": "@d",
            "kesan": "Kakaknya sangat bersahabat",
            "pesan": "Sukses selalu di karier dan kuliahnya!"
        },
        {
            "nama": "Kakak E",
            "nim": "122450004",
            "umur": "22",
            "asal": "Surabaya",
            "alamat": "Jl. Pahlawan",
            "hobbi": "Musik, traveling",
            "sosmed": "@e",
            "kesan": "Kakaknya sangat inspiratif",
            "pesan": "Teruskan impian kakak!"
        },
    ]
    display_images_with_data(gambar_urls, data_list)