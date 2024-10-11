import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True
#Mencegah datanya berubah menjadi default

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)
#homepage itu adalah variabel
#st.page adalah komponen di streamlit untuk membuat halaman
#st.page ini butuh argumen; Halaman Utama/halaman_utama.py (path directory); 

Mahasiswa1 = st.Page(
    "Buku Kating/051_Fiodora Alysa Juandi.py",
    title="051 - Fiodora Alysa Juandi",
    icon=":material/person:",
)
#Mahasiswa1 akan mengakses data yang bernama Kemas Veriandra yang foldernya disimpan di Buku Kating

Mahasiswa2 = st.Page(
    "Buku Kating/020_Try Yani Rizki Nur Rohmah.py",
    title="020 - Try Yani Rizki Nur Rohmah",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/001_Eksanty Febriana.py",
    title="001 - Eksanty Febriana",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/117_Anwar Muslim.py",
    title="117 - Anwar Muslim",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/014_Deva Anjani Khayyuninafsyah.py",
    title="014 - Deva Anjani Khayyuninafsyah",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/103_Rut Junita Sari Siburian.py",
    title="103 - Rut Junita Sari Siburian",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/050_Ahmad Rizky.py",
    title="050-Ahmad Rizky",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/007_Devyna Sonya Palupi Sanjaya.py",
    title="007-Devyna Sonya Palupi Sanjaya",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()
#if state adalah logic di mana kita bisa berpindah-pindah page tanpa data-data kita ini hilang atau berubah
#Halaman utama akan menampung homepage
#Buku Kating akan menampung Nama mahasiswa
#try me akan menampung kreasI dan kreasII