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
            "MedKraf"
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
            "people-fill"
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

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dQHbiGzXsxjbp_TguJNgfUNwDGx3JHRx",
            "https://drive.google.com/uc?export=view&id=1dGkdjR-B4Gx2r2J_IQfzsJpzJS2B9Iw5",
            "https://drive.google.com/uc?export=view&id=1dJ6438dvFzjRXr25KzO1lmxha8P4YSit",
            "https://drive.google.com/uc?export=view&id=1dOVQunnUCWK-DLOoIkwcMqIi70_gzwmu",
            "https://drive.google.com/uc?export=view&id=1dHmV6_bfmkavCuMYwf7V695ZC59GD1cB",
            "https://drive.google.com/uc?export=view&id=1dJspqeENS7eJioLC6jmakfEVc6EBK2UO",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/file/d/1bR2tiDjlAqOvwHCTU3_GSrBUtDnZ9VHv/view",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Denger Musik",
                "sosmed": "@gumilangtkharisma",
                "kesan": "banyak wawasannya dan keren ",
                "pesan": "Sukses terus ya bang, makasih insightnya,",
                "jabatan" : "Ketua himpunan",  # 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "wah kakaknya dari pagaralam, sama dong",
                "pesan": "semangatt kak sukses terus",  
                "jabatan" : " Sekretaris Umum" # 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Denger Musik",
                "sosmed": "@hrtfdlh",
                "kesan": "cantik dan ramah",
                "pesan": "semangat menjalani hidupnya kak",
                "jabatan" : "Bendahara umum",  # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "keren dan asik",
                "pesan": "semangat kuliahnya bang", 
                "jabatan" : "Sekretaris Jendral", # 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "baik dan ramah",
                "pesan": "semangat ya kak kuliahnya, semoga cita-citanya tercapai", 
                "jabatan" : "Sekretaris 1", # 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "1214500030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Baca",
                "sosmed": "@nadillaandr26",
                "kesan": "aura bendaharanya kerasa sih",
                "pesan": "semangat kak, jangan pantang menyerah",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YsYqLKVux0RmnPxZYAG6YbsAN0NMoPE1",
            "https://drive.google.com/uc?export=view&id=1Zjm7pbxsAfPPM20DZquOcEKItwlF9qIg",
            "https://drive.google.com/uc?export=view&id=1Yp3ixkRgSmDTHftHE24wyhtdDIOv3_m-",
            "https://drive.google.com/uc?export=view&id=1ZQTq9rjB7QXPNCD1NlMoIKGRCtT6elOn",
            "https://drive.google.com/uc?export=view&id=1Z2U3NJra7D_bJMxCGIYINZDCOzXQzbHW",
            "https://drive.google.com/uc?export=view&id=1YsO4rie16bT8whF7EhNHmc625siauKI1",
            "https://drive.google.com/uc?export=view&id=1Yq9_2hPoi7ghSnbVopFnIXZins_SB7Rq",
            "https://drive.google.com/uc?export=view&id=1ZHZ10ttXtBy4idifcA5IdFQ2d7VDqAlQ",
            "https://drive.google.com/uc?export=view&id=1a2_K6BqZ97eK6SndhruqF2I6mF3_GF6k",
            "https://drive.google.com/uc?export=view&id=1YyYb7gJShL6p7Q_uJlL9Mzu8JRjh1_S0",
            "https://drive.google.com/uc?export=view&id=1ZkZQWHZYa3uOVilfgX034vVf77bLLbuZ",
            "https://drive.google.com/uc?export=view&id=1ZjmDZJG89t782VjNTKNS8es0hKCrFQl4",
            "https://drive.google.com/uc?export=view&id=1Z-dzi2e0sh3MDZFSsgD2oNHvLsnPMA0w",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Tanya sama GPT",
                "sosmed": "@trimurniaa",
                "kesan": "Kakaknya lucu dan cantik banget pinter lagi",
                "pesan": "semangat kuliahnya kak,semoga cita-citanya tercapai",
                "jabatan" : "Ketua Badan Legislatif", #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Puasa Senin Kamis",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakanya keren dan pinter juga penyampaiannya",
                "pesan": "Semangat kuliahnya kak, semoga makin rajin  ", 
                "jabatan" : "Sekretaris", # 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "@wlsbn0",
                "kesan": "Ramah banget, baik, lucu",
                "pesan": "semangat kak, jangan menyerah ", 
                "jabatan" : "Bendahara", # 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "Kakaknya ramahh, asik,baik",
                "pesan": "semangat terus kuliahnya kakak, jangan mudah menyerah", 
                "jabatan" : "Kepala Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": " @dylebee",
                "kesan": "Bagus sekali kak namanya, orangnya juga cantik",
                "pesan": "semangat ya kuliahnya jangan putus asa kak", 
                "jabatan" : "Kepala Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat Malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
                "jabatan" : "Kepala Komisi 3 Media Legislatif", # 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al waqiah setiap magrib",
                "sosmed": " @ansftynn_",
                "kesan": "Manis banget kakaknya, ramah juga",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Feryadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya sepertinya famous yah",
                "pesan": "semangat kuliahnya kak, semoga lulus tepat waktu", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "pengen ketagihan baca alquran juga jadinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin baca al-qurannya", 
                "jabatan" : "Anggota Komisi 1 Legislatif", # 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya sangat ramah kelihatannya",
                "pesan": "semangat main kucingnya bang", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "asik dan lucu banget kakaknya",
                "pesan": "semangat terus kak, semoga cepet ketemu sinyal gedung f nya kak", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "hobinya berkelas semua kak",
                "pesan": "semangat kuliahnya kak, jangan putus asa ", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "baik dan ramah",
                "pesan": "semangat kuliahnya bang, makin sukses ", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "Senator":

    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eyTdLAGoFJiSrOugyS6fxkLfhb2ZOSaq",
            "https://drive.google.com/uc?export=view&id=1bR2tiDjlAqOvwHCTU3_GSrBUtDnZ9VHv",
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
                "kesan": "kakaknya keren dan menginspirasi ",
                "pesan": "semangat terus kak",
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
                "kesan": "publik speakingnya keren",
                "pesan": "semangat terus bang, lancar kuliahnya", 
                "jabatan": " Tim Senator",
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1prXGR8RyNjDM3Sy5vEOBDZ4H10IFNCWd",
            "https://drive.google.com/uc?export=view&id=1B1GXfON-VrUbLByT0w9XPg44Hr9Z8Pd-",
            "https://drive.google.com/uc?export=view&id=1O3sWojv6hXAAnjXiaTs1NZ4WKvgkTvxD",
            "https://drive.google.com/uc?export=view&id=17mTlJ44drDbRXOQR9_sq7swlS5qPE3iP",
            "https://drive.google.com/uc?export=view&id=17_2pltn-3Cld_hL01mv8MT9_QLmgNn7D",
            "https://drive.google.com/uc?export=view&id=1sM1GdFtRc8kIkfkUa_xcdqKqI3BlOegD",
            "https://drive.google.com/uc?export=view&id=14PWOTaZkW0YG6MzN1dFEqx5rTkthxWh_",
            "https://drive.google.com/uc?export=view&id=1BBLRtPG7cvoB6SfCAkmr6s7ofG1mJPaP",
            "https://drive.google.com/uc?export=view&id=1G-3C0FLTCzoejHDT7SnbJwl139sz8vui",
            "https://drive.google.com/uc?export=view&id=1a9SfXUvHxHFKwLTJmgAC1-LFBaZ5Pkcl",
            "https://drive.google.com/uc?export=view&id=1lWH-f1GmCrd0DAPmjx1nVCpL6k7pEUGw",
            "https://drive.google.com/uc?export=view&id=17bCwSPZFStGFmo_0xzYOxZTFdHZZrROP",
            "https://drive.google.com/uc?export=view&id=17hL2rAT1zF1e3v6Xn7fYzQGG4NPeqUqz",
            "https://drive.google.com/uc?export=view&id=17e8cUoJ6j-9eS-LRaMUsUaPBssnh3Sy5",
            "https://drive.google.com/uc?export=view&id=17dIi-BzGlkagxm3DFBY4kCNzslI7cDJ_",
            "https://drive.google.com/uc?export=view&id=17UORcKAOLIXmk9nePFqjCgQXGQuO1IPm",
            "https://drive.google.com/uc?export=view&id=17UORcKAOLIXmk9nePFqjCgQXGQuO1IPm",
            "https://drive.google.com/uc?export=view&id=17NAfEvZ24EC_07mem6oYBRxYGrb0-v1k",
            "https://drive.google.com/uc?export=view&id=17Ro5jRPevwn9abDM46eOtXxNOX3NF6QZ",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": " Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Keren banget bang",
                "pesan": "Semangat bang, semoga aku bisa keren kayak abang",
                "jabatan" : "Kepala Departemen PSDA", #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Asik banget kakanya, lucu juga",
                "pesan": "Semangat kuliahnya kak, jangan lupa istirahat", 
                "jabatan" : "Sekretaris Departemen PSDA", # 1
            },
            {
                "nama": "Deyvan Loxefal ",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya kelihatan berbakat sekali",
                "pesan": "Semangat bang jangan lupa istirahat", 
                "jabatan" : "Kepala Divisi Manjakat", # 1
            },
            {
                "nama": " Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya cantik dan tegas",
                "pesan": "Jangan lupa istirahat kak, jaga kesehatan", 
                "jabatan" : "Kepala Divisi Kaderisasi", # 1
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Keren bang sangat memotivasi kami",
                "pesan": "Selalu jadi orang baik yang rajin menolong", 
                "jabatan" : "Kepala Divisi Olahraga dan Perlombaan", # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren bang",
                "pesan": "Semoga semakin rajin ngaspraknya bang", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main game",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya keliatan gamers ternyata memang hobi main game",
                "pesan": "Semakin rajin ya bang belajarnya", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Music taste nya bagus kak",
                "pesan": "Semangat belajarnya kak, semoga akademiknya emakin meningkat ", 
                "jabatan" : " Bendahara Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Baik kakaknya, ramah jugaa",
                "pesan": "Semangat kak kuliahnya, sukses selalu", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abangnya baik ramah suaranya bagus",
                "pesan": "Semangat kuliahnya bang,bahagia dan sukses selalu", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak kerenn sangattt, sukanya sama stylenya",
                "pesan": "Keren selalu kakk", 
                "jabatan" : "Staff Divisi Manajemen Minat dan Bakat", # 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak tegas dan berwibawa",
                "pesan": "Semangat kuliahnya kak, semoga segala kebaikan menyertai kakak", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": " 122450001",
                "umur": "20",
                "asal": " Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Terus memotivasi kami kak, semangat terus", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abangnya humble dan asik",
                "pesan": "Semangat mengejar akademiknya bang", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "1224500418",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Sukses selalu kak dalam segala hal", 
                "jabatan" : "Staff Divisi Kaderisasi", # 1
            },
             {
                "nama": "Gede Moena",
                "nim": " 121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya ramah dan tidakk sombong",
                "pesan": "Semangat dalam menjalani hari-hari bang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": " Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakak baik, ramah dan rajin olahraga",
                "pesan": "Semoga semakin jago kak renangnya", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Sehat dan bahagia selalu bang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
             {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakaknya pintar dan baik hati",
                "pesan": "Sukses selalu kak dalam berbagai bidang", 
                "jabatan" : "Staff Olahraga dan Perlombaan", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()
elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AmjM16_eVl1qty-qpQeBsUY49LsjKbhK",
            "https://drive.google.com/uc?export=view&id=1AyXNRk6IZxj-gIU8q-fTO3YXJn2Gg7NP",
            "https://drive.google.com/uc?export=view&id=1B4eLheFbhA4ruPVrDBlg18XlDm8g5nru",
            "https://drive.google.com/uc?export=view&id=1BfBlMNtO0dho_LgPxY0-jEq22bjyb2mq",
            "https://drive.google.com/uc?export=view&id=1BA7dmAstBfKRnoeJpBHkAGFQXxR_eAtq",
            "https://drive.google.com/uc?export=view&id=1B-jewURMfkZFdE_5pMNBgAQ_S7UyBnyd",
            "https://drive.google.com/uc?export=view&id=1BYE68XZEBrE1JGkP_-5d-J39UxrrXJFV",
            "https://drive.google.com/uc?export=view&id=1BOffgNHu9XJT1QmQSohU0lwEonq1iA5F",
            "https://drive.google.com/uc?export=view&id=1BtKZRqlUOdyy3pwYlOqf4YD1IUQib67H",
            "https://drive.google.com/uc?export=view&id=1B-jABB9FkUVrpeJNrIp3kg_MbRkCRSrA",
            "https://drive.google.com/uc?export=view&id=1B3swyCJ56-wLv03T1wDzLZoefMRfRLHu",
            "https://drive.google.com/uc?export=view&id=1B2A0ogX6R6BNlnRoqFURIs8UFT_FHWXD",
            "https://drive.google.com/uc?export=view&id=1AmLN6mAtCwT_x7U_wT4zd9axmHHkLY9O",
            "https://drive.google.com/uc?export=view&id=1BbP6L4fG3kQ7pOD4yzutPe21q1o2-fQs", 
            "https://drive.google.com/uc?export=view&id=1AxdAyTSRlLDwt8dEPcWlF4UZllG2qQYP",
            "https://drive.google.com/uc?export=view&id=1BsAswkH4KNTo9L7M1yt0GApzQNuhxFGC",
            "https://drive.google.com/uc?export=view&id=1BdMv-Srt_XddhzPy9m9YZxaTBeWJ52vN",
            "https://drive.google.com/uc?export=view&id=1BUy1UNIZ7JaFnUZ72WF6dhV2_xOJn684",
            "https://drive.google.com/uc?export=view&id=1B1dDb6Nf5bwpRNQdMQzVr89ymSv33rnM",

        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Ambisius dan keren",
                "pesan": "semangat bang",
                "jabatan" : "Kepala Departemen Mikfes", #1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya baik dan ramah sekali",
                "pesan": "Semangat dan sukses selalu kak", 
                "jabatan" : "Sekretaris Departement", # 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Keren abangnya jago olahraga",
                "pesan": "Semangat terus bang olahraganya semoga semakin rajin", 
                "jabatan" : " Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Baik dan ramah",
                "pesan": "Sukses selalu bang, jangan lupa semangat", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame ",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Ramah dan suka menolong",
                "pesan": "Selalu memotivasi kami ya bang", 
                "jabatan" : "Staff Divisi Club dan Komuitas", # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Keren kakaknya sepertinya aktif sekali di organisasi",
                "pesan": "Semangat kak semoga akademiknya semakin meningkat", 
                "jabatan" : "Staff Divisi Club dan Komunitas", # 1
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Pintar dan baik hati abangnya",
                "pesan": "Semoga kesuksesan selalu menyertai abang", 
                "jabatan" : "Kepala Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": " ramah dan solutif abangnya",
                "pesan": "Semangat abang pj materi kelompok kami cosval", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Ramah dan baik banget kak",
                "pesan": "Sukses selalu kak dalam berbagai hal", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "-",
                "sosmed": "@dindanababan_",
                "kesan": "Keren kakaknyaa",
                "pesan": "Semangat menjalani hri-hari kak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurna",
                "sosmed": "@marletacornelia",
                "kesan": "Pinter kak marletta, kenal dari pas TPB jadi tutor matdas TPB 2",
                "pesan": "Semangat terus kak, semoga akademiknya semakin meningkat", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "keren daa tidak sombong",
                "pesan": "Bahagia terus ya kakak", 
                "jabatan" : "Staff Divisi Pusat Inovasi dan Kajian Akademik", # 1
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": " 121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "ramah dan baik",
                "pesan": "Sukses selalu bang, terus memberi motivasi kepada kami", 
                "jabatan" : "Kepala Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "abangnya ramah dan keren",
                "pesan": "Sukses selalu bang ", 
                "jabatan" : "@egistr", # 1
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Keren banget bang ",
                "pesan": "Selalu membimbing kami ya bang", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Baik kakaknya dan cantik",
                "pesan": "Jangan pernah bosan ngajarin kami ya kak", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
             {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Baik dan ramah abangnya",
                "pesan": "Sukses selalu bang", 
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
             {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Keren dan baik abangnya",
                "pesan": "semangat bang",
                "jabatan" : "Staff Divisi Survei dan Riset", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kKYpuvasaPZ-KA2SyWkbhV1yrRAJLaLL",
            "https://drive.google.com/uc?export=view&id=1jrUlgTzJ4K_Ss0l8sDHADTCLrIdQr_Hm",
            "https://drive.google.com/uc?export=view&id=1kR4AoAW1PdQ-UxV3Ur8w9ASbVZHiQpjW",
            "https://drive.google.com/uc?export=view&id=1mAr7SH0O3Z7BVbPblqyK_-ptMG_yv6aj",
            "https://drive.google.com/uc?export=view&id=1kOSvVlUvc6tBs5BdKZIx-IPSwnvmInbS",
            "https://drive.google.com/uc?export=view&id=1kRePwe5QPFxwmc5ScXtJi0xoHfym18lT",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1iymWqYUBHT-nehmfjXA0u9z0Bw-daCyW",
            "https://drive.google.com/uc?export=view&id=1kQ13Ko4HpPIcAqxbvMocyq5Bn8MHwtcb",
            "https://drive.google.com/uc?export=view&id=1kOf3G9twV2eG-63-vhqMyDG6-zS5sOjQ",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=17oBJNl-TLjMoie-wVmEmSjAfsfnnFDFS",
            "https://drive.google.com/uc?export=view&id=1jrE7yUuAcjG7LgftBo7KQDaVQ3ded3sf",
            "https://drive.google.com/uc?export=view&id=1jm4trQa9IeZ0jKttPyuCPcGqygvcGGgd/",
            "https://drive.google.com/uc?export=view&id=1dTPEOwDYGxIYXeK2DlpjlwQVLCatHqWG",
            "https://drive.google.com/uc?export=view&id=1k0iMyYLWsDuIouJW4cQTI32C2yki5wdA",
            "https://drive.google.com/uc?export=view&id=1b-06Tb7F_sOwzSZK24U_0ldXoAoNUIZ3",
            "https://drive.google.com/uc?export=view&id=1b0cPkvm14ikH03bCoRncORIfqVUKL0EX",
            "https://drive.google.com/uc?export=view&id=1jon-L2x3E67gvpf06xoPoBiGufac_djX",
            "https://drive.google.com/uc?export=view&id=1k-1YK4sanrLJAUVxjfRsotJdfM-2NaLJ",
            
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosmed": "@yogyst",
                "kesan": "Abangnya baik dan berbagi ilmu",
                "pesan": "Semakin sukses ya bang",
                "jabatan" : "Kepala Departemen Eksternal", #1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "keren dan aktif",
                "pesan": "semangat selalu kak", 
                "jabatan" : "Sekretaris Departement", # 1
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "asik banget",
                "pesan": "sukses dan ceria terus kak", 
                "jabatan" : "Kepala Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Keren bang",
                "pesan": "Semangat selalu kuliahnya bang", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "kak dea! daplok yang selalu suportif",
                "pesan": "Semangat terus ya kakk", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Asik banget dan lucu kakk",
                "pesan": "Semangat terus kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Keren dan selalu aktif di organisasi",
                "pesan": "Semangat ya kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Cantik dan ramah sekali kakaknya",
                "pesan": "selalu ceria dan gembira kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya baik dan unik",
                "pesan": "Bahagia terus kak", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Keren dan selalu aktif berkegiatan",
                "pesan": "Jangan lupa istirahat bang, semoga semangatnya selalu membara", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
             {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya baik dan keren",
                "pesan": "Sukses selalu kak di dalam hal apapun", 
                "jabatan" : "Staff Divisi Hubungan Luar", # 1
            },
             {
                "nama": "Rizky Adrian Bennovry",
                "nim": "1214500731",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "baik hati abangnya",
                "pesan": "Selalu semangat bang, sukses", 
                "jabatan" : "Kepala Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Asik dan keren banget",
                "pesan": "Tetap jadi orang baik bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya ramah dan cocok sekali di pengmas",
                "pesan": "Tetap jadi orang yang ramah kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Baik sekali kakaknya",
                "pesan": "Tetap pertahankan semangat yang berkobar itu kak", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Keren banget bang dan baik hati",
                "pesan": "Jangan lupa istirahat dan semangat bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Baik, humble sekali kakk",
                "pesan": "Tetap pertahankan akademiknya kakakk", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": " Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Baik hati dan namanya bagus sekali kak",
                "pesan": "Sukses selalu kakk", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Baik dan sangat memberi motivasi bang",
                "pesan": "Bahagia selalu bang", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
             {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": " @tria_y062",
                "kesan": "Baik dan ramahh",
                "pesan": "Semangat kak dalam menjalani seluruh kegiatan ", 
                "jabatan" : "Staff Divisi Pengabdian Masyarakat", # 1
            },
           
           
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "",
                "kesan": "Abangnya asik dana kece",
                "pesan": "Semangat kuliahnya bang, tetap fokus",
                "jabatan" : "", #1
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Manis bangett kakk, NIM nya sama kayak aku hihi",
                "pesan": "Semangat ya kak, tetap ramah", 
                "jabatan" : "Sekretaris", # 1
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakaknya baik, pertanyaanku semua terjawab",
                "pesan": "Sehat selalu kak", 
                "jabatan" : "Kepala Divisi Media & Konten", # 1
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "Abangnya asik dan kece",
                "pesan": "Keren banget bang", 
                "jabatan" : "Kepala Divisi PDD", # 1
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "",
                "pesan": "", 
                "jabatan" : "Kepala Divisi Visual Desain", # 1
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Suka banget sama outfit kakak, cocok banget di divisi media & konten",
                "pesan": "Lancar terus kuliahnya kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya keliatan rajin organisasi",
                "pesan": "Jangan lupa istirahat kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Keren banget kakaknya",
                "pesan": "Jangan lupa istirahat kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Lucu asik banget kakaknya",
                "pesan": "Jaga kesehatan kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Keren banget kak, pasti jago ngoding",
                "pesan": "Ajarin aku ngoding dong kak", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Baik banget kakaknya",
                "pesan": "Ayo kak nonton bareng", 
                "jabatan" : "Anggota Divisi Media & Konten", # 1
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Baik abangnya",
                "pesan": "Ajarin aku foto foto dong kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "kakaknya baik dan ramah",
                "pesan": "semangat kuliahnya kak, tetap pertahankan jadi orang baiknya", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya asik banget",
                "pesan": "Semangat kuliahnya bang", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya keren dan asik",
                "pesan": "Semangat bang, jaga kesehatan", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Rajin banget abangnya hobi membaca buku",
                "pesan": "Semangat kuliahnya bang, tetap baik hati", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya kelihatan rajin dan sekaliii",
                "pesan": "Sehat selalu kak", 
                "jabatan" : "Anggota Divisi Visual Desain", # 1
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya asik banget",
                "pesan": "Jangan lupa bahagia kak", 
                "jabatan" : "Anggota Divisi PDD", # 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen SSD":

    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Keren banget abangnya sangat berambisi mencari uang",
                "pesan": "Semoga makin banyak uang bang",
                "jabatan" : "Kepala Departemen SSD", #1
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya asal dari Metro sama kayak aku",
                "pesan": "Semangat kak, semoga makin banyak uang", 
                "jabatan" : "Sekretaris Departemen SSD", # 1
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Keren banget kakaknya jago ngitung uang",
                "pesan": "Semangat kak menghitung uangnya", 
                "jabatan" : "Kepala Divisi KWU", # 1
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Sering ketemu abangnya, produktif banget ya bang",
                "pesan": "Semangat bang walaupun produktif jangan lupa jaga kesehatan", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": " 122450110",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Keren abangnya asik juga",
                "pesan": "Semangat bang", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukitting",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abangnya rapih banget, suka",
                "pesan": "Semangat terus bang kuliahnya", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya manis banget dan juga humble",
                "pesan": "Semangat kak kuliahnya, tetap semangatt", 
                "jabatan" : "Staff KWU", # 1
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Keren kak jadi kepala sponsor",
                "pesan": "Semoga kerennya nular ke aku ya kak", 
                "jabatan" : "Kepala Divisi Sponsor", # 1
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya manis banget dan asikk",
                "pesan": "Semangat kuliahnya kak, tetap jadi orang baik", 
                "jabatan" : "Staff sponsor", # 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": " Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya kalem banget",
                "pesan": "Semangat bang kuliahnya", 
                "jabatan" : "Staff sponsor", # 1
            },
           
           

        ]
        display_images_with_data(gambar_urls, data_list)

    SSD()




    

    



# Tambahkan menu lainnya sesuai kebutuhan
