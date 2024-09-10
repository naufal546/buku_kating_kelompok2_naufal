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
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
                ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
                in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
                officia deserunt mollit anim id est laborum.
            </div>""",
            unsafe_allow_html=True,
        )
        layout("https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_")

    home_page()

elif menu == "About Us":
    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)

        # Example data for images and bios
        image_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ] * 5  # Repeated URL for simplicity
        data_list = [
            {
                "nama": "Ahmad Rizky",
                "sebagai": "Pak Lurah",
                "nim": "123450050",
                "fun_fact": "Gampang tidur",
                "motto_hidup": "Gampang, tidur!",
            },
            # More entries...
        ]

        display_images_with_data(image_urls, data_list)

    about_page()