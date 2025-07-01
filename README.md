# 🌱 ETL-Assessment-Green-Finance

| Nama            | No Absen       | Kelompok |
|------------------|----------------|----------|
| Asfa Asfialana   | 10.037.DB2025  | III      |

---

## 🏢 Green Finance Data Analysis

## 1. 🌍 Latar Belakang

Sustainability atau keberlanjutan merupakan konsep yang berkembang pesat saat ini. Awal mula konsep ini disebabkan karena kebutuhan tinggi pada sumber daya alam yang terbatas serta banyaknya aktivitas masyarakat yang dilakukan ternyata memberikan efek yang buruk bagi alam. Perubahan iklim (climate change) adalah hasil negatif dari fenomena tersebut, hal ini sudah banyak terjadi di Indonesia, dilansir dari CNN Indonesia (2021) bukti perubahan iklim diantaranya gelombang panas ekstrem, meningkatnya suhu di Sumatra dan Kalimantan sebesar 4°C dan berkurangnya curah hujan sebesar 12%, terjadinya kekeringan dan banjir di beberapa daerah, kenaikan air laut di pesisir, siklon tropis, dan penurunan panen bahan pokok yang jika dibiarkan semua akan menyebabkan penurunan PDB per kapita sampai 31%. Pada 2015, menurut Amidjaya & Widagdo (2020) Perserikatan Bangsa Bangsa (PBB) merespon dinamika alam tersebut dengan membentuk agenda aksi Sustainable Development Goals (SDGs) yang ditargetkan akan tercapai pada 2030.

![


Selain itu berdasarkan databoks dari *International Energy Agency (IEA)*:

> 🌡️ Emisi karbon dioksida (CO₂) dari sektor energi dan industri global mencapai **37,6 gigaton (Gt)** CO₂ pada **2024**.  
> Emisi tersebut meningkat **0,8%** dibanding **2023** (*year-on-year/yoy*),  
> sekaligus menjadi **rekor tertinggi baru** seperti terlihat pada grafik.

![gambar1](https://github.com/Asfa-Asfialana/ETL-Assessment-Green-Finance/blob/main/Data/gambar1.png)

---

Green finance merupakan bentuk implementasi dari Sustainable Development Goals (SDGs) dalam sektor bisnis atau perusahaan yang saat ini mulai banyak diperhatikan. Pengertian Green finance menurut Urban & Wójcik (2019) adalah proses pengalokasian sumber modal atau aktivitas investasi keuangan yang mempedulikan perlindungan lingkungan, perubahan iklim, energi ramah lingkungan, dan pengelolaan yang bertanggung jawab di segala sektor sedangkan menurut Volz et al. (2015) mendefinisikan green finance sebagai serangkaian aktivitas investasi atau peminjaman modal yang mempertimbangkan dampak lingkungan dan turut melestarikan lingkungan, dapat diketahui green finance merupakan aktivitas pengelolaan keuangan yang memfokuskan pada kelestarian lingkungan bukan hanya persoalan keuntungan atau kerugian semata. Pada beberapa literasi, green finance memiliki banyak sebutan lain seperti sustainability finance, environmental finance, dan sebagainya. Sampai saat ini penelitian masih banyak dilakukan untuk mengetahui penyebab maupun dampak dari green finance di perusahaan.

Green finance adalah salah satu alat yang Krusial dalam usaha menangani dampak perubahan iklim. untuk mencapai SDGs (Sustainable Development Goals) yang telah ditetapkan oleh PBB. Green finance (keuangan ramah lingkungan) berperan sebagai layanan keuangan yang mendorong keberlanjutan ekologi, perlawanan terhadap iklim dan efisiensi energi. Green finance menjadi salah satu cara untuk mendukung pelaku bisnis yang peduli lingkungan melalui penyediaan dana atau pinjaman. (Rahmanisa, 2023). Green finance mengatur aliran modal menuju proyek-proyek peduli terhadap lingkungan, dan pada akhirnya akan menghasilkan peningkatan produksi suatu perusahaan berdasarkan kegiatan yang ramah lingkungan, seperti energi terbarukan, efisiensi energi, pengelolaan limbah, dan proyek-proyek yang berkontribusi pada mitigasi perubahan iklim dan pembangunan berkelanjutan. Selain itu, Green finance memandu bisnis industri agar menggunakan lebih sedikit energi dengan kemampuan mengelola sumber daya keuangan guna memperoleh manfaat ekonomi dan lingkungan (Ronaldo & Suryanto, 2022). 

---

## 2. 📝 Rumusan Masalah yang akan dianalisis

1. Bagaimana mengidentifikasi proyek **PLTS** yang memiliki efisiensi pengurangan CO₂ tertinggi per satuan **juta rupiah investasi**?
2. Berapa rata-rata pengurangan emisi CO₂ dari seluruh proyek **PLTM** untuk menilai dampak lingkungan kolektifnya?
3. Bagaimana merancang alat yang dapat menampilkan **status lahan dan tingkat konflik sosial** berdasarkan **Project_ID**?
4. Proyek mana saja yang memiliki **daya tarik investasi tinggi** namun dengan **tingkat konflik sosial rendah** sehingga dapat meminimalkan risiko?
5. Bagaimana menghitung **total investasi** untuk proyek-proyek yang memiliki **efisiensi lokasi tinggi**?
6. Bagaimana membangun **alat komputasi efisiensi CO₂** yang dapat digunakan kembali dan memiliki kemampuan **penanganan kesalahan** (error handling)?
7. Bagaimana menghitung **rata-rata keluaran energi** dari proyek-proyek terpilih, dengan memperhitungkan **data yang hilang** (missing data)?
8. Bagaimana memprediksi tingkat **daya tarik investasi** ("High", "Medium", "Low") untuk proyek-proyek baru berdasarkan variabel seperti **GDP_Growth**, **CO₂_Reduction**, dan **Investment_Cost**?

---

## 3. 🎯 Tujuan Analisis

- Mengukur efisiensi pengurangan CO₂ dari proyek PLTS per satuan biaya investasi.
- Menentukan dampak lingkungan kolektif dari proyek PLTM melalui penghitungan rata-rata pengurangan emisi CO₂.
- Mengembangkan alat input berbasis **Project_ID** untuk mengecek **status lahan** dan **tingkat konflik sosial**.
- Mengidentifikasi proyek yang menarik secara finansial dan rendah konflik sosial sebagai prioritas investasi.
- Menghitung total investasi pada proyek-proyek yang memiliki **lokasi strategis** dan efisien.
- Membangun alat komputasi efisiensi CO₂ yang **tangguh**, **dapat digunakan ulang**, dan **andal**.
- Menganalisis rata-rata **energy output** meskipun terdapat data tidak lengkap.
- Membangun model prediktif klasifikasi daya tarik investasi berdasarkan variabel-variabel ekonomi dan lingkungan.

---

## 4. 🌱 Manfaat Analisis

- Memberikan **rekomendasi berbasis data** untuk mendukung kebijakan investasi energi terbarukan pemerintah.
- Menyediakan **alat bantu analisis praktis** untuk stakeholder dan pengambil kebijakan.
- Mempermudah proses seleksi dan pemantauan proyek yang **berdampak besar dan rendah risiko**.
- Mendorong perencanaan proyek yang lebih **strategis, efisien, dan berkelanjutan**.
- Meningkatkan efisiensi penggunaan anggaran negara untuk mendukung **transisi energi hijau**.

---

