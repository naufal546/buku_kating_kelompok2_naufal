import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Cache the image loading function to improve performance
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)  # Fix image orientation
        return img
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")
        return None

def display_images_with_data(image_urls, data_list):
    # Load all images
    images = [load_image(url) for url in image_urls]

    # Display each image and its associated data
    for i, img in enumerate(images):
        if img is not None:
            col1, col2, col3 = st.columns([1, 2, 1])  # Layout columns to center image
            with col2:
                st.image(img, use_column_width=True)  # Show the image in the center

            if i < len(data_list):  # Show data associated with each image
                st.write(f"**Nama**: {data_list[i]['nama']}")
                st.write(f"**Sebagai**: {data_list[i]['sebagai']}")
                st.write(f"**NIM**: {data_list[i]['nim']}")
                st.write(f"**Fun Fact**: {data_list[i]['fun_fact']}")
                st.write(f"**Motto Hidup**: {data_list[i]['motto_hidup']}")
        else:
            st.warning(f"Gambar {i + 1} gagal dimuat.")  # Error handling if the image fails to load

# Display the website header using HTML for custom styling
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# URLs for images to be displayed
image_urls = [
    "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx",
    "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"
]

# Layout function to center images with custom width
def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Use a 1:2:1 ratio for the columns
    with col2:
        img = load_image(url)
        if img:
            st.image(img, use_column_width=True)  # Display image in the center
        else:
            st.error("Failed to load image.")

# Display the images using the layout function
for url in image_urls:
    layout(url)

# Custom Streamlit option menu
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {"font-size": "15px", "text-align": "left", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

# Handle menu selection
menu = streamlit_menu()

if menu == "Home":
    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True)
        st.markdown(
            """<div style="text-align: justify;">
                Cosval adalah singkatan dari cosine similiarity value, 
            dan dalam konteks kelompok kami, cosval memiliki pengertian bagaimanapun setiap anggota dari kelompok kami itu memiliki nilai 
            dan pandangannya masing-masing, kami tetap bersatu demi mencapai tujuan yang
            satu pula yaitu cosval yang satu dan bermaslahat.
            </div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        layout("https://drive.google.com/uc?export=view&id=1v3pP4xrpB-Wtot97192_Mltj4YCRE0Lf")
        st.markdown(
            """<div style="text-align: justify;">Cosval adalah kelompok 2 dari kaderisasi CEO HMSD dengan pendamping kelompok bernama bang rendi juga ka dea.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":
    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>Cosval Punya Cerita!!!</h1>", unsafe_allow_html=True)

        # Example data for images and bios
        image_urls = [
            "https://drive.google.com/uc?export=view&id=17IHwnjun_lUPkqyYlOTA2c6rCzXMF6j1",
            "https://drive.google.com/uc?export=view&id=1HopTjgZ13YReoCuWO4o5Fq06RuulYTeR",
            "https://drive.google.com/uc?export=view&id=1akLNriez_lrmJ_NO_YbDSAHQ-DJQn2yj",
            "https://drive.google.com/uc?export=view&id=1Q7Rs5epvN8usr5QHfUNtfvdMJT6xhBjt",
            "https://drive.google.com/uc?export=view&id=1rjgDBRcs65bYxr8LvfZQDCxiXlbncldT",
            "https://drive.google.com/uc?export=view&id=1Aqc4h6KVwSWlbX-xHhJWkhBM_cAj85RC",
            "https://drive.google.com/uc?export=view&id=1YLCvZiZWUyio25SpYRddOKM9o7qMtEYS",
            "https://drive.google.com/uc?export=view&id=1KiPuU6oKNhlZ5f6srQ5uHyH67DJ4BYHD",
            "https://drive.google.com/uc?export=view&id=1KevS5s4qJh77sU3yNfkwMt8MUZBIwh98",
            "https://drive.google.com/uc?export=view&id=1Km6LlwVy9XQMU9eBuMjrG2EcsgoX6G46",
            "https://drive.google.com/uc?export=view&id=1eGfyDbA8G4MauY8mf2xfC_DoBHFE13kv",
            "https://drive.google.com/uc?export=view&id=1p5c2pu-zlI6u9irYj_ipJfhA4J4E4FRu"
        ] # Repeated URL for simplicity
        data_list = [
            {
                "nama": "Ahmad Rizky",
                "sebagai": "Pak Lurah",
                "nim": "123450050",
                "fun_fact": "Gampang tidur",
                "motto_hidup": "Gampang, tidur!",
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "sebagai": "Anggota",
                "nim": "123450116",
                "fun_fact": "Aku sebenarnya pemalu",
                "motto_hidup": "Tetap belajar walau perlahan",
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "sebagai": "Bu Lurah",
                "nim": "123450007",
                "fun_fact": "dengerin bernadya 24/7",
                "fun_fact": "Dengerin lagu Bernadya 24/7",
                "motto_hidup": "everything happens for a reason",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "sebagai": "Anggota",
                "nim": "123450048",
                "fun_fact": "softboy abizzzz",
                "motto_hidup": "kill the past",
            },
            {
                "nama": "Rahma Oktavia Albar",
                "sebagai": "Anggota",
                "nim": "123450003",
                "fun_fact": "pecinta mie ayam",
                "motto_hidup": "jangan pernah menyerah sebelum mencoba",
            },
            {
                "nama": "Intan Nursyabani",
                "sebagai": "Anggota",
                "nim": "123450081",
                "fun_fact": "tempe for life",
                "motto_hidup": "worst maybe could be the best, because almost everything is paradox",
            },
            {
                "nama": "Vania Claresta",
                "sebagai": "Anggota",
                "nim": "123450029",
                "fun_fact": "beli barang karena lucu",
                "motto_hidup": "with God all things are possible -Matthew 19:26",
            },
            {
                "nama": "Fiodora Alysa Juandi",
                "sebagai": "Anggota",
                "nim": "123450051",
                "fun_fact": "ga suka duren",
                "motto_hidup": "banyak banyak bersyukur aja",
            },
            {
                "nama": "Malika Azzahra Salsabila",
                "sebagai": "Anggota",
                "nim": "123450090",
                "fun_fact": "Minum kopi biar bisa tidur",
                "motto_hidup": "When life gives you lemons, don't make lemonade. Make life take the lemons back.",
            },
            {
                "nama": "Ken Gracya Waoma",
                "sebagai": "Anggota",
                "nim": "123450045",
                "fun_fact": "lebih memprioritaskan untuk beristrahat",
                "motto_hidup": "all progress takes place outside the comfort zone",
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "sebagai": "Anggota",
                "nim": "123450102",
                "fun_fact": "suka lupa tempat parkirin motor",
                "motto_hidup": "Be greather than averange",
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "sebagai": "Anggota",
                "nim": "123450020",
                "fun_fact": "suka makan telur",
                "motto_hidup": "Do Good, Receive Good",
            },
            # More entries...
        ]

        display_images_with_data(image_urls, data_list)

    about_page()