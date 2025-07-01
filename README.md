# 🌱 ETL-Assessment-Green-Finance

| Nama            | No Absen       | Kelompok |
|------------------|----------------|----------|
| Asfa Asfialana   | 10.037.DB2025  | III      |

---

## 🏢 Green Finance Data Analysis

## 1. Pendahuluan

### 1.1 🌍 Latar Belakang

Sustainability atau keberlanjutan merupakan konsep yang berkembang pesat saat ini. Awal mula konsep ini disebabkan karena kebutuhan tinggi pada sumber daya alam yang terbatas serta banyaknya aktivitas masyarakat yang dilakukan ternyata memberikan efek yang buruk bagi alam. Perubahan iklim (climate change) adalah hasil negatif dari fenomena tersebut, hal ini sudah banyak terjadi di Indonesia, dilansir dari CNN Indonesia (2021) bukti perubahan iklim diantaranya gelombang panas ekstrem, meningkatnya suhu di Sumatra dan Kalimantan sebesar 4°C dan berkurangnya curah hujan sebesar 12%, terjadinya kekeringan dan banjir di beberapa daerah, kenaikan air laut di pesisir, siklon tropis, dan penurunan panen bahan pokok yang jika dibiarkan semua akan menyebabkan penurunan PDB per kapita sampai 31%. Pada 2015, menurut Amidjaya & Widagdo (2020) Perserikatan Bangsa Bangsa (PBB) merespon dinamika alam tersebut dengan membentuk agenda aksi Sustainable Development Goals (SDGs) yang ditargetkan akan tercapai pada 2030.

![gambar2](https://github.com/Asfa-Asfialana/ETL-Assessment-Green-Finance/blob/main/Data/gambar2.png)

Selain itu berdasarkan databoks dari *International Energy Agency (IEA)*:

> 🌡️ Emisi karbon dioksida (CO₂) dari sektor energi dan industri global mencapai **37,6 gigaton (Gt)** CO₂ pada **2024**.  
> Emisi tersebut meningkat **0,8%** dibanding **2023** (*year-on-year/yoy*),  
> sekaligus menjadi **rekor tertinggi baru** seperti terlihat pada grafik.

![gambar1](https://github.com/Asfa-Asfialana/ETL-Assessment-Green-Finance/blob/main/Data/gambar1.png)

Green finance merupakan bentuk implementasi dari Sustainable Development Goals (SDGs) dalam sektor bisnis atau perusahaan yang saat ini mulai banyak diperhatikan. Pengertian Green finance menurut Urban & Wójcik (2019) adalah proses pengalokasian sumber modal atau aktivitas investasi keuangan yang mempedulikan perlindungan lingkungan, perubahan iklim, energi ramah lingkungan, dan pengelolaan yang bertanggung jawab di segala sektor sedangkan menurut Volz et al. (2015) mendefinisikan green finance sebagai serangkaian aktivitas investasi atau peminjaman modal yang mempertimbangkan dampak lingkungan dan turut melestarikan lingkungan, dapat diketahui green finance merupakan aktivitas pengelolaan keuangan yang memfokuskan pada kelestarian lingkungan bukan hanya persoalan keuntungan atau kerugian semata. Pada beberapa literasi, green finance memiliki banyak sebutan lain seperti sustainability finance, environmental finance, dan sebagainya. Sampai saat ini penelitian masih banyak dilakukan untuk mengetahui penyebab maupun dampak dari green finance di perusahaan.

Green finance adalah salah satu alat yang Krusial dalam usaha menangani dampak perubahan iklim. untuk mencapai SDGs (Sustainable Development Goals) yang telah ditetapkan oleh PBB. Green finance (keuangan ramah lingkungan) berperan sebagai layanan keuangan yang mendorong keberlanjutan ekologi, perlawanan terhadap iklim dan efisiensi energi. Green finance menjadi salah satu cara untuk mendukung pelaku bisnis yang peduli lingkungan melalui penyediaan dana atau pinjaman. (Rahmanisa, 2023). Green finance mengatur aliran modal menuju proyek-proyek peduli terhadap lingkungan, dan pada akhirnya akan menghasilkan peningkatan produksi suatu perusahaan berdasarkan kegiatan yang ramah lingkungan, seperti energi terbarukan, efisiensi energi, pengelolaan limbah, dan proyek-proyek yang berkontribusi pada mitigasi perubahan iklim dan pembangunan berkelanjutan. Selain itu, Green finance memandu bisnis industri agar menggunakan lebih sedikit energi dengan kemampuan mengelola sumber daya keuangan guna memperoleh manfaat ekonomi dan lingkungan (Ronaldo & Suryanto, 2022). 


### 1.2. 📝 Rumusan Masalah yang akan dianalisis

Rumusan masalah yang akan kita lakukan analisis dalam proyek analisis green finance kali ini adalah :

1. Bagaimana mengidentifikasi proyek **PLTS** yang memiliki efisiensi pengurangan CO₂ tertinggi per satuan **juta rupiah investasi**?
2. Berapa rata-rata pengurangan emisi CO₂ dari seluruh proyek **PLTM** untuk menilai dampak lingkungan kolektifnya?
3. Bagaimana merancang alat yang dapat menampilkan **status lahan dan tingkat konflik sosial** berdasarkan **Project_ID**?
4. Proyek mana saja yang memiliki **daya tarik investasi tinggi** namun dengan **tingkat konflik sosial rendah** sehingga dapat meminimalkan risiko?
5. Bagaimana menghitung **total investasi** untuk proyek-proyek yang memiliki **efisiensi lokasi tinggi**?
6. Bagaimana membangun **alat komputasi efisiensi CO₂** yang dapat digunakan kembali dan memiliki kemampuan **penanganan kesalahan** (error handling)?
7. Bagaimana menghitung **rata-rata keluaran energi** dari proyek-proyek terpilih, dengan memperhitungkan **data yang hilang** (missing data)?
8. Bagaimana memprediksi tingkat **daya tarik investasi** ("High", "Medium", "Low") untuk proyek-proyek baru berdasarkan variabel seperti **GDP_Growth**, **CO₂_Reduction**, dan **Investment_Cost**?


### 1.3. 🎯 Tujuan Analisis

Analisis green finance yang dilakukan bertujuan :

- Mengukur efisiensi pengurangan CO₂ dari proyek PLTS per satuan biaya investasi.
- Menentukan dampak lingkungan kolektif dari proyek PLTM melalui penghitungan rata-rata pengurangan emisi CO₂.
- Mengembangkan alat input berbasis **Project_ID** untuk mengecek **status lahan** dan **tingkat konflik sosial**.
- Mengidentifikasi proyek yang menarik secara finansial dan rendah konflik sosial sebagai prioritas investasi.
- Menghitung total investasi pada proyek-proyek yang memiliki **lokasi strategis** dan efisien.
- Membangun alat komputasi efisiensi CO₂ yang **tangguh**, **dapat digunakan ulang**, dan **andal**.
- Menganalisis rata-rata **energy output** meskipun terdapat data tidak lengkap.
- Membangun model prediktif klasifikasi daya tarik investasi berdasarkan variabel-variabel ekonomi dan lingkungan.
- Sebagai syarat menyelesaikan Asessment Task Eco Techno Leader

### 1.4. Manfaat Analisis

Diharapkan hasil analisis green finance ini dapat memberi manfaat, seperti :

- Memberikan **rekomendasi berbasis data** untuk mendukung kebijakan investasi energi terbarukan pemerintah.
- Menyediakan **alat bantu analisis praktis** untuk stakeholder dan pengambil kebijakan.
- Mempermudah proses seleksi dan pemantauan proyek yang **berdampak besar dan rendah risiko**.
- Mendorong perencanaan proyek yang lebih **strategis, efisien, dan berkelanjutan**.
- Meningkatkan efisiensi penggunaan anggaran negara untuk mendukung **transisi energi hijau**.

---

## 2. Kajian Pustaka

### 2.1 Green Finance 🌱

Green finance atau biasanya disebut dengan sustainability finance menurut Urban & Wójcik (2019) adalah proses pengalokasian sumber daya modal atau kegiatan investasi keuangan yang peduli terhadap perlindungan lingkungan, perubahan iklim, energi ramah lingkungan, dan pengelolaan yang bertanggung jawab di semua sektor. Di Indonesia perkembangannya dimulai pada 2009 melalui UU No 32 Tahun 2009 Tentang Perlindungan dan Pengelolaan Lingkungan Hidup, pemerintah Indonesia mengatur kegiatan usaha wajib untuk melewati proses Analisis Mengenai Dampak Lingkungan (AMDAL) yang mana kegiatan usaha tersebut perlu mengidentifikasi potensi dampak negatif terhadap lingkungan serta mempertimbangkan kritik dan saran dari masyarakat sekitar untuk dijadikan dasar penyusunan rencana pengelolaan dan pemantauan lingkungan hidup. Bank Indonesia telah memasukan persyaratan AMDAL sebagai kriteria dalam menyalurkan modal pada pelaku usaha yang mengajukan kebutuhan dana pada perbankan. Peraturan Bank Indonesia No 14/15/PBI/2012 Tentang Penilaian Kualitas Aset Bank Umum yang diikuti dengan Surat Edaran Bank Indonesia No 15/28/DPNP mengenai Penilaian Kualitas Aset Bank Umum mendorong sektor perbankan untuk mempertimbangkan faktor kelayakan lingkungan dalam menilai prospek usaha atau proyek yang akan didanai. 

Implementasi green finance saat ini masih belum memiliki pedoman yang jelas baik secara nasional maupun internasional. Tidak adanya pedoman baku yang harus diikuti oleh pelaku usaha dalam menjalankan green finance membuat mereka menjalankan prinsip tersebut dalam garis besar saja atau penerapan green/sustainability finance hanya didasarkan pada pengurangan dampak pencemaran dan perusakan lingkungan saja padahal penerapan yang dapat dilakukan bisa lebih luas lagi, seperti membantu masyarakat untuk sadar dalam menjaga lingkungan atau melakukan kemitraan yang berbasis pada kelestarian lingkungan. Tidak adanya panduan atau standar yang jelas mengenai kebenaran perusahaan dalam mengimplementasikan green finance memberikan hal yang tidak baik karena dapat memicu praktik manipulatif, perusahaan yang melakukan kampanye green finance bisa saja dilakukan hanya untuk formalitas publik atau mengikuti peraturan saja tanpa benar-benar melakukan. Sebaliknya, tidak ada panduan dalam penerapan green finance bisa saja memberikan tudingan negatif pada perusahaan atau pelaku usaha yang sebenarnya menerapkan praktik tersebut tanpa mempublikasikannya.

Walaupun tidak ada pedoman yang jelas bukan berarti penerapan green finance tidak dapat dievaluasi untuk diketahui kebenarannya, salah satu cara untuk menganalisis adalah menggunakan python. Analisis Green Finance dapat dilakukan secara efektif menggunakan bahasa pemrograman Python, mengingat kemampuannya yang luas dalam mengelola, memproses, dan menganalisis data multidimensi yang melibatkan aspek keuangan, lingkungan, sosial, dan spasial. Dengan menggunakan Python, proses analisis Green Finance menjadi lebih efisien, reproducible, dan transparan, terutama dalam konteks evaluasi efisiensi investasi hijau, perhitungan emisi CO₂, pengukuran dampak sosial, serta klasifikasi daya tarik proyek berbasis data. Pendekatan ini juga memungkinkan pengembangan alat analisis yang dapat digunakan ulang (reusable tools) dan mampu menangani data yang tidak lengkap atau tidak konsisten melalui teknik data cleaning dan error handling.

### 2.2 Financial Dataset

Financial Dataset adalah kumpulan data yang berisi informasi keuangan tentang proyek-proyek energi (seperti PLTS dan PLTM). Dataset ini digunakan untuk:

- Mengevaluasi kelayakan investasi proyek
- Menilai risiko dan potensi keuntungan
- Membandingkan efisiensi dana antar proyek

### 2.3 Social Dataset

Berisi data sosial di sekitar lokasi proyek, seperti:
- `Land_Status`: Status kepemilikan lahan (Adat, Negara, Swasta)
- `Community_Support`: Dukungan masyarakat (%)
- `Population_Density`: Kepadatan penduduk
- `Tingkat_Konflik`: Potensi konflik sosial (Low, Medium, High ⚠️)

**Tujuan:** Mengukur risiko sosial dan potensi penerimaan masyarakat terhadap proyek.
 
### 2.4 Economic Dataset

Menyajikan indikator ekonomi untuk menilai kelayakan investasi:
- `GDP_Growth`: Pertumbuhan ekonomi lokal (%)
- `Interest_Rate`: Suku bunga (%)
- `Bond_Yield`: Imbal hasil obligasi hijau (%)
- `Daya_Tarik_Investasi`: Peringkat daya tarik proyek (High/Medium/Low)

**Tujuan:** Mengukur potensi dan resiko ekonomi dari proyek hijau.

### 2.5 Enviromental Dataset

Berisi informasi tentang dampak dan manfaat lingkungan, seperti:
- `CO2_Reduction`: Jumlah pengurangan emisi karbon (kg)
- `Energy_Output`: Energi yang dihasilkan (kWh)
- `Environmental_Risk_Index`: Indeks risiko lingkungan
- `Peringkat_Dampak`: Skor dampak proyek (Low/Medium/High 🌿)

**Tujuan:** Menilai efisiensi dan kontribusi proyek terhadap keberlanjutan lingkungan.

### 2.6 Geospatial Dataset

Menyediakan informasi spasial dan lokasi proyek:
- `Latitude` / `Longitude`: Koordinat geografis proyek
- `Efisiensi_Lokasi`: Efisiensi lokasi (High/Medium/Low)
- `Jarak_Ke_Jaringan`: Jarak ke jaringan listrik terdekat (km)

**Tujuan:** Menilai kelayakan lokasi proyek dari sisi teknis dan distribusi energi.

---

## 3. 📊 Hasil dan Pembahasan


