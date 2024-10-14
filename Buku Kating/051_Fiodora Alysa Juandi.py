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
            "https://drive.google.com/uc?export=view&id=1srIhnLGLnoCzJDfrFOSIvYGLmoTb1N0N",
            "https://drive.google.com/uc?export=view&id=1hh4eLuXHajIDqPYB4Xg9T_uRA0yyNNJQ",
            "https://drive.google.com/uc?export=view&id=1G3V6WLQor-wTPjIiu98adBSbx5P8Hmn9",
            "https://drive.google.com/uc?export=view&id=1PKii0kMkRVpSiYcmcAsdrvVQlsWdKjzQ",
            "https://drive.google.com/uc?export=view&id=1RRjn3p7obs4yOGGXKDNgUB8_tqeQ3IYB",
            "https://drive.google.com/uc?export=view&id=1UuxrTMYjtH_augK2B6w5dKSHYQ_HQjam",
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
                "kesan": "Cara komunikasi abangnya keren",
                "pesan": "Semoga cepat lulus bang",
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
                "kesan": "Kakaknya lucu bangettt",
                "pesan": "semangat kuliahnya semoga cepat lulus kak",  
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
                "kesan": "Kakaknya pendiam dan kalem",
                "pesan": "Jangan patah semangat kakak",
                "jabatan" : "Bendahara umum",  # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": " 121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@nadillaandr26",
                "kesan": "Abangnya keren public speakingnya",
                "pesan": "semangat bang kuliahnya, jangan patah semangat", 
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
                "kesan": "Kakaknya keliatan pintar",
                "pesan": "semangat kak kuliahnya, dan tidak mudah menyerah", 
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
                "kesan": "Sama sama asal metro hihihi",
                "pesan": "semangat kak kuliahnya, sukses selalu",  
                "jabatan" : "Bendahara 1", # 1
            },




        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1u2LnV0mTQogIYs4y9nftJceib_8rjSrt",
            "https://drive.google.com/uc?export=view&id=1Mjv7Hga6C_GT-S1tJWjZhrGg12Ze4ntE",
            "https://drive.google.com/uc?export=view&id=1wkpz2p_sipQPYPdGS5hwhWRe-tSAoNNF",
            "https://drive.google.com/uc?export=view&id=1xRy_zNrdLppEq6BUKeBSLo04S0HPtxKV",
            "https://drive.google.com/uc?export=view&id=1I7mV2KgTNE6InLtXJwCxTaBogJNxxYiS",
            "https://drive.google.com/uc?export=view&id=1jJnU3nibKggPNHJfRqPIbAsULvgzpfEe",
            "https://drive.google.com/uc?export=view&id=1oEAaXpKZw4xNByqG1NwP520JezNQoU8w",
            "https://drive.google.com/uc?export=view&id=1y2H_EdRfGoBF5dhMKM3HFcLseHVBd-T0",
            "https://drive.google.com/uc?export=view&id=1igUoJXdyDoLnEIP4Y8u31g-LR-7vZuCK",
            "https://drive.google.com/uc?export=view&id=1lMXPna-siKEj7pU3JzAGKgFsPZqfOUKk",
            "https://drive.google.com/uc?export=view&id=1rzVo9Ah-7RBOM5YYZVoXSFg4mlUoK44t",
            "https://drive.google.com/uc?export=view&id=1uID-TsF0YGU6TZEofMUZPaJUG36bB6O3",
            "https://drive.google.com/uc?export=view&id=1kDwjHSnxHMgcCd1PM9K3eIsG1XMTBuRk",
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
                "kesan": "Kakaknya cantik, ramah, baik",
                "pesan": "semangat kuliahnya kakak, tetap jadi orang baik",
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
                "kesan": "Baik banget kakaknya, sgt humble",
                "pesan": "Semangat kuliahnya kak", 
                "jabatan" : "Sekretaris", # 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "wlsbn0",
                "kesan": "Ramah banget kakanya, baikk pula",
                "pesan": "semangat ya kak, tetap ramahh", 
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
                "kesan": "MasyaAllah kak pertahankan hobinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin mengerjakan tugas", 
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
                "kesan": "Abangnya baik, kalem, dan ramah",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
                "jabatan" : "Anggota Komisi 2 Aspirasi dan Pengawasan", # 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "Kakaknya kelihatan aktif organisasi bangettt",
                "pesan": "Ramahh banget kak Dheaa", 
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
                "kesan": "Baik kakanya",
                "pesan": "semangat kuliahnya kak, tetap pertahankan jadi orang baik", 
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
                "kesan": "Abangnya keliatan seperti orang pintar, memang pintar",
                "pesan": "semangat kuliahnya kak, tetap pertahankan akademiknya", 
                "jabatan" : " Anggota Komisi 3 Legislatif", # 1
            },
             


        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "MedKraf":

    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nPBOX0ccPNoJ8JXr4L6H4iE_f6-HZ0rs",
            "https://drive.google.com/uc?export=view&id=1t10zFtR3pAukNaSYcpS3wRws-64Dxxj3",
            "https://drive.google.com/uc?export=view&id=1scrWn9MzuC2gCkt99tMdRtlVuQh7wl25",
            "https://drive.google.com/uc?export=view&id=1_FidCGCCXGLgFbY8gDY4170STjrFFlXl",
            "https://drive.google.com/uc?export=view&id=1mdvkfsYJ8WLZ6QSfP2ZfBIAo4FJiD8hf",
            "https://drive.google.com/uc?export=view&id=1L_-NCwykbCnGE64ycYlxXYpLGeQF91m9",
            "https://drive.google.com/uc?export=view&id=1FPcW3xij4NQdMnQSk5NRarz-9sQogcg1",
            "https://drive.google.com/uc?export=view&id=12fQY3aieQJFXhQlN9ryJg4-0IQlGwyTH",
            "https://drive.google.com/uc?export=view&id=1zG9d9PrnMvMcpKsBH8vQxHxL5MOsdHh",
            "https://drive.google.com/uc?export=view&id=1POdKZLiuP3MEPtIsGHd3x8mBZ-GWrVLt",
            "https://drive.google.com/uc?export=view&id=1XSvnTFVBD0k5IjFT2sD-ObQRDaEpB_LQ",
            "https://drive.google.com/uc?export=view&id=13QUBn-PBhnCqX9kzAuhTWxgS_CdcUjOi",
            "https://drive.google.com/uc?export=view&id=1l_3a7dIzcaDnfZUqdEdJW_EXApuSWgCy",
            "https://drive.google.com/uc?export=view&id=1nED8Efxr47wOyxQMQArv0DPyExuaZBJn",
            "https://drive.google.com/uc?export=view&id=1gBTwdeOa8BB94BAcqpy8FdC8Mag7pvdY",
            "https://drive.google.com/uc?export=view&id=1vwfdR3MBxM0neon0ZFWZpxmpIsSqSZUC",
            "https://drive.google.com/uc?export=view&id=1XaCYi_G8nbdNPd6ItNpnIEQbSq4pDzac",
            "https://drive.google.com/uc?export=view&id=1aPkfEWqZvt6J8_SwFWNoRyrso1O8_J-O",
            "https://drive.google.com/uc?export=view&id=13ENqy-WDdx7_WTBMn2vGKikJsd3zXXLD",
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
                "jabatan" : "Kepala Departemen", #1
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
                "kesan": "Keren abangnya pasti jago ngoding",
                "pesan": "Semangat bang ngodingnya", 
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
            "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobi": "",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakaknya kalem banget dan baik hati ",
                "pesan": "Semangat kak dan bahagia terus ya", 
                "jabatan" : "Anggota Divisi PDD", # 1
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
            "https://drive.google.com/uc?export=view&id=1mMb9JSDLeze6qudPfMWPW-NV9msWGsqJ",
            "https://drive.google.com/uc?export=view&id=1upOiVJBc1rED7sEfG1D4F11HfMWngLYt",
            "https://drive.google.com/uc?export=view&id=16wNCsus9_2NvnVPrVMbhKiW28JeOIeMJ",
            "https://drive.google.com/uc?export=view&id=1K0Rf227mUJSPTQHEAQQ0v_dfT8BQQ4LG",
            "https://drive.google.com/uc?export=view&id=1V26dD6Iu9vIUI7Z7hHsJruGQ6_jDOTMi",
            "https://drive.google.com/uc?export=view&id=1HwfBhKOuUAEM6FXpFlw3L5lGxOhltl0I",
            "https://drive.google.com/uc?export=view&id=1wgJcptKnbItQU-yTBKr5htnR2Gvxn3bv",
            "https://drive.google.com/uc?export=view&id=17os67zDHkdGPiJcB-Tyxp9TV-w9wapXs",
            "https://drive.google.com/uc?export=view&id=1sW_X0feS-ma29FaXvDCgP21MwbQTjSMY",
            "https://drive.google.com/uc?export=view&id=1e40AFoEiOV_eMRiTWk2feDqbJBJGLHWF",
            
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

elif menu == "Departemen PSDA":

    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WRelsiMEzrHw-12Ruo8ApWSbgGaF05Fy",
            "https://drive.google.com/uc?export=view&id=1jM3cwRrMCBS1c6O4BCyrugmewztRrqgi",
            "https://drive.google.com/uc?export=view&id=1kud2i-6AKaGdbYw_lElBzBfdtAjO16RS",
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
        ]
        display_images_with_data(gambar_urls, data_list)

    PSDA()


    

    



# Tambahkan menu lainnya sesuai kebutuhan
