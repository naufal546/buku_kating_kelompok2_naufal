import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown(
    """<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True
)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)


# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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


@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None


@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":

    def Senator():
        gambar_urls = [
            ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/file/d/1bR2tiDjlAqOvwHCTU3_GSrBUtDnZ9VHv/view",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Denger Musik",
                "sosmed": "@gumilangtkharisma",
                "kesan": "Cara komunikasi abangnya keren",
                "pesan": "Semoga cepat lulus bang",  # 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",  # 1
            },
            {
                "nama": "Kakak CC",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",  # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Senator":

    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Senator",
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": " Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "-",
                "pesan": "-", 
                "jabatan": " Tim Senator",
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "MIKFES":

    def Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21 Tahun",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Kepala Departement",
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21 Tahun",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": " Memasak",
                "sosmed": "@anovavona",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Sekretaris Departement",

            },
            {
                "nama": " Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": " 20",
                "asal": "Tulang Bawang",
                "alamat": " Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Club dan Komunitas",
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Teluk Betung ",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Club dan Komunitas",
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " 122450031",
                "umur": "19 Tahun",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame  ",
                "hobbi": "Main Game",
                "sosmed": "@mregiiii_",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Club dan Komuitas",
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira ",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Club dan Komunitas",
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing ",
                "nim": "121450107",
                "umur": "20 Tahun",
                "asal": "Jakarta",
                "alamat": "Kemiling ",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21 Tahun",
                "asal": "Bukittinggi",
                "alamat": "Korpri ",
                "hobbi": " ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21 Tahun",
                "asal": " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20 Tahun",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Main Game",
                "sosmed": "@dindanababan_",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20 Tahun",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20 Tahun",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": " 122450072",
                "umur": "20 Tahun",
                "asal": "Palembang",
                "alamat": "Belwis ",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik",
            },
            {
                "nama": " Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": " Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Kepala Divisi Survei dan Riset",
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20 Tahun",
                "asal": " Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Survei dan Riset",
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20 Tahun",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr ",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Survei dan Riset",
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20 Tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama ",
                "sosmed": "@pratiwifebiya",
                "kesan": "-",
                "pesan": "-",
                "jabatan": "Staff Divisi Survei dan Riset",
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20 Tahun",
                "asal": "Lampung",
                "alamat": "Karang Anyar ",
                "hobbi": " Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Survei dan Riset",
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21 Tahun",
                "asal": "Banten",
                "alamat": " Sukarame",
                "hobbi": " Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "-",
                "pesan": "-",
                "jabatan": " Staff Divisi Survei dan Riset",
            },
        


    
            
           
        ]
        display_images_with_data(gambar_urls, data_list)

    Mikfes()


# Tambahkan menu lainnya sesuai kebutuhan
