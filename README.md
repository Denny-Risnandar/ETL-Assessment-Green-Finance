# 🌱 ETL-Assessment-Green-Finance

| Nama               | No Absen       | Kelompok |
|--------------------|----------------|----------|
|Alif Nur Rahman     | 10.028.DB2025  | III      |
|Asfa Asfialana      | 10.037.DB2025  | III      |
|Denny Risnandar     | 09.000.DB2025  | III      |
|Ihsan Ahsanul Amala | 09.000.DB2025  | III      |

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

1. Mengukur efisiensi pengurangan CO₂ dari proyek PLTS per satuan biaya investasi.
2. Menentukan dampak lingkungan kolektif dari proyek PLTM melalui penghitungan rata-rata pengurangan emisi CO₂.
3. Mengembangkan alat input berbasis **Project_ID** untuk mengecek **status lahan** dan **tingkat konflik sosial**.
4. Mengidentifikasi proyek yang menarik secara finansial dan rendah konflik sosial sebagai prioritas investasi.
5. Menghitung total investasi pada proyek-proyek yang memiliki **lokasi strategis** dan efisien.
6. Membangun alat komputasi efisiensi CO₂ yang **tangguh**, **dapat digunakan ulang**, dan **andal**.
7. Menganalisis rata-rata **energy output** meskipun terdapat data tidak lengkap.
8. Membangun model prediktif klasifikasi daya tarik investasi berdasarkan variabel-variabel ekonomi dan lingkungan.
9. Sebagai syarat menyelesaikan Asessment Task Eco Techno Leader

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

Green finance atau biasanya disebut dengan sustainability finance menurut Urban & Wójcik (2019) adalah proses pengalokasian sumber daya modal atau kegiatan investasi keuangan yang peduli terhadap perlindungan lingkungan, perubahan iklim, energi ramah lingkungan, dan pengelolaan yang bertanggung jawab di semua sektor. Di Indonesia perkembangannya dimulai pada 2009 melalui UU No 32 Tahun 2009 Tentang Perlindungan dan Pengelolaan Lingkungan Hidup, pemerintah Indonesia mengatur kegiatan usaha wajib untuk melewati proses Analisis Mengenai Dampak Lingkungan (AMDAL) yang mana kegiatan usaha tersebut perlu mengidentifikasi potensi dampak negatif terhadap lingkungan serta mempertimbangkan kritik dan saran dari masyarakat sekitar untuk dijadikan dasar penyusunan rencana pengelolaan dan pemantauan lingkungan hidup.

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

## 3. 📊 Metodologi

### 3.1 Metode Analisis

Penelitian ini menggunakan pendekatan kuantitatif berbasis data untuk mengevaluasi kelayakan dan dampak proyek-proyek energi hijau melalui kerangka kerja Green Finance. Terdapat lima dimensi utama yang dianalisis: finansial, lingkungan, sosial, ekonomi, dan geospasial.

Tahapan Penelitian:
**1. Pengumpulan Data**
  Lima dataset dikompilasi, masing-masing mewakili dimensi Green Finance:

- Financial Dataset
- Environmental Dataset
- Social Dataset
- Economic Dataset
- Geospatial Dataset

**2.Pra-Pemrosesan Data**

- Mengimpor data dari file .xlsx
- Pembersihan data: menangani nilai hilang, duplikat, dan format tidak konsisten
- Normalisasi dan transformasi kolom jika diperlukan

### 3.2 Implementasi 

Proyek ini dibangun menggunakan bahasa Python 3.12 dan dijalankan di lingkungan Jupyter Notebook dalam manajemen lingkungan Conda. Struktur direktori dan teknologi yang digunakan sebagai berikut:

- Python 3.12
- Conda (Environment Management)\
- Jupyter Notebook
- Pandas, NumPy (manipulasi data)
- Matplotlib(visualisasi)
- OpenPyXL / xlrd (baca file Excel)

### 3.3 📁 Struktur Proyek

| Folder / File                  | Deskripsi                                                  |
|-------------------------------|-------------------------------------------------------------|
| `📁 notebooks/`                | Direktori untuk Jupyter Notebook                           |
| └── `analisis.ipynb`          | Notebook utama yang berisi proses eksplorasi dan analisis  |
| `📁 data/`                     | Folder berisi semua dataset proyek                         |
| ├── `financial_dataset.xlsx`  | Data investasi dan keuangan proyek                         |
| ├── `environmental_dataset.xlsx` | Data pengurangan emisi CO₂ dan aspek lingkungan        |
| ├── `social_dataset.xlsx`     | Data sosial seperti konflik dan status lahan               |
| ├── `economic_dataset.xlsx`   | Data dampak ekonomi proyek secara makro                    |
| └── `geospatial_dataset.csv`  | Data lokasi geografis dan efisiensi spasial proyek         |
| `README.md`                   | Dokumentasi utama proyek                                   |

----

## 4. Hasil dan Pembahasan

### 4.1 Evaluasi Efisiensi Reduksi Emisi CO₂ pada Proyek PLTS

Analisis ini bertujuan untuk mengukur **efisiensi reduksi emisi karbon dioksida (CO₂)** terhadap biaya investasi pada proyek-proyek PLTS (Pembangkit Listrik Tenaga Surya). Efisiensi dihitung dengan rumus:

$$
\mathrm{Efisiensi}_{CO_2} = \frac{\mathrm{CO2\ Reduction\ (ton)}}{\mathrm{Investment\ Cost\ (Rp)}} = \frac{\mathrm{CO2\ Reduction}}{\mathrm{InvestmentCost} \times 1{,}000{,}000}
$$

Di mana:
- **CO₂ Reduction** = total emisi CO₂ yang berhasil dikurangi (dalam ton)
- **Investment Cost** = jumlah biaya investasi proyek (dalam miliar rupiah)

```
for _, row in plts_df.iterrows():
    ratio = row["CO2_Reduction"] / (row["Investment_Cost"] * 1_000_000)
    category = "High" if ratio >= 0.5 else "Low"
    print(f"{row['Project_ID']}: {ratio:.4f} ({category})")
```

Selanjutnya, setiap proyek diklasifikasikan menjadi:
- `"High"` jika efisiensi ≥ 0.5 ton CO₂ per juta rupiah
- `"Low"` jika efisiensi < 0.5 ton CO₂ per juta rupiah

Berikut hasil klasifikasi proyek PLTS:

- PLTS-NTT-001: 0.0005 (Low)
- PLTS-JATIM-001: 0.0004494830944413924 (Low)
- PLTS-SULS-001: 0.00047808764940239046 (Low)
- PLTS-NTB-001: 0.00044444444444444447 (Low)
- PLTS-JABW-001: 0.0004318181818181818 (Low)


Semua proyek memiliki nilai efisiensi di bawah 0.5 ton CO₂ per juta rupiah.
Hasil evaluasi menunjukkan bahwa **tidak ada proyek PLTS yang mencapai kategori efisiensi "High"** berdasarkan ambang batas yang ditentukan pemerintah. Rata-rata efisiensi hanya berada pada kisaran **0.0004–0.0005**, jauh di bawah target 0.5.

Beberapa kemungkinan penyebab efisiensi rendah:
- **Biaya investasi sangat besar**, terutama di daerah terpencil atau pulau-pulau kecil
- **Skala proyek masih kecil**, sehingga dampak pengurangan emisinya tidak sebanding dengan investasi
- Teknologi panel surya yang digunakan mungkin belum maksimal dalam efisiensi

### 4.2 Rata-rata Pengurangan Emisi CO₂ Proyek PLTM

Analisis ini bertujuan untuk menghitung **rata-rata pengurangan emisi karbon dioksida (CO₂)** yang dihasilkan oleh proyek-proyek **PLTM (Pembangkit Listrik Tenaga Minihidro)** berdasarkan data pada `Environmental_Dataset.xlsx`.

Dalam soal ini, digunakan pendekatan berbasis Python dengan penekanan pada **penggunaan `for loop`, `if` condition, dan `list`** untuk memproses data baris demi baris. Berikut tahapan yang dilakukan:

1. **Menyiapkan list kosong** untuk menyimpan nilai `CO2_Reduction` dari proyek PLTM.
2. **Melakukan iterasi (`for loop`)** terhadap seluruh baris pada dataset.
3. **Menggunakan `if` condition** untuk memfilter hanya proyek yang:
   - Project_ID diawali `"PLTM"`
   - Nilai `CO2_Reduction` tidak kosong
4. Menambahkan nilai valid ke dalam list.
5. **Menghitung total dan rata-rata** dari nilai-nilai dalam list tersebut.

```
python
# Langkah 1–4: Iterasi dan filter data
pltm_co2_list = []

for _, row in env_df.iterrows():
    project_id = row["Project_ID"]
    if isinstance(project_id, str) and project_id.startswith("PLTM"):
        co2_reduction = row["CO2_Reduction"]
        if pd.notnull(co2_reduction):  # Pastikan tidak kosong
            pltm_co2_list.append(co2_reduction)

# Langkah 5: Hitung rata-rata jika ada data valid
if len(pltm_co2_list) > 0:
    total_co2 = sum(pltm_co2_list)
    average_co2 = total_co2 / len(pltm_co2_list)
    print(f"Average CO2 Reduction for PLTM Projects: {average_co2:.0f} tons CO2e")
else:
    print("Tidak ada proyek PLTM yang valid ditemukan.")
```

Rata-rata pengurangan emisi CO₂ untuk proyek PLTM adalah sebesar 34.600 ton CO₂e. Nilai ini dihitung berdasarkan data proyek PLTM yang valid dalam dataset, dengan menyaring Project_ID yang diawali "PLTM".



### 4.3 Pemeriksaan Status Lahan dan Tingkat Konflik Sosial Proyek

Program ini dirancang untuk membantu pemerintah dan pemangku kepentingan memeriksa **status lahan** dan **tingkat konflik sosial** berdasarkan input *Project_ID*, dengan pendekatan interaktif berbasis `while loop` dan `user input`.Fitur ini berfokus pada aspek **Social Governance** dalam kerangka Green Finance, khususnya terkait:

- Legalitas dan kepemilikan lahan proyek
- Risiko sosial dan potensi konflik di lapangan

Analisis ini bertujuan melatih penggunaan **`while loop` dan pengolahan input pengguna** dalam Python. Berikut langkah-langkah utama:

1. **Membaca data sosial** dari `Social_Dataset.xlsx`
2. **Menyimpan data ke dalam dictionary** (`soc_data`) agar pencarian cepat
3. Menggunakan **`while loop`** untuk:
   - Meminta input pengguna berulang kali
   - Menampilkan status lahan dan tingkat konflik jika Project_ID ditemukan
   - Menampilkan pesan “Project not found” jika tidak valid
4. **Program berhenti** saat pengguna mengetik `"0"` atau `"Done"`

```python
# Tahap 1–2: Siapkan dictionary data sosial
soc_data = {}
for _, row in soc_df.iterrows():
    pid = row['Project_ID']
    land_status = row['Land_Status']
    konflik = row['Tingkat_Konflik']
    soc_data[pid] = (land_status, konflik)

# Tahap 3–4: Loop interaktif untuk pencarian data
while True:
    user_input = input("Enter Project_ID (or '0' to finish): ")
    
    if user_input.strip() == "0":
        break
    
    if user_input in soc_data:
        land_status, konflik = soc_data[user_input]
        print(f"{user_input} - Land Status: {land_status}, Tingkat Konflik: {konflik}")
    else:
        print("Project not found")
```
Contoh ouput dari program yang sudah dibuat, misalnya :

```
Enter Project_ID (or '0' to finish): PLTS-NTT-001
PLTS-NTT-001 - Land Status: Adat, Tingkat Konflik: High

Enter Project_ID (or '0' to finish): PLTM-JABAR-002
PLTM-JABAR-002 - Land Status: Pemerintah, Tingkat Konflik: Low

Enter Project_ID (or '0' to finish): INVALID-ID
Project not found

Enter Project_ID (or '0' to finish): 0
```

Program berhasil memenuhi kebutuhan evaluasi sosial proyek energi secara interaktif.
Dengan pendekatan Python yang sederhana namun efektif, fitur ini:

- 🔍 Menyediakan informasi penting secara real-time
- 🛡️ Membantu mitigasi risiko konflik sosial sejak tahap perencanaan
- 📊 Menunjukkan pentingnya data sosial dalam kerangka Green Finance yang berkelanjutan

### 4.4 Identifikasi Proyek Potensial Rendah Risiko

Analisis ini bertujuan untuk membantu pemerintah dan pemangku kebijakan dalam **mengidentifikasi proyek energi terbarukan** yang:

- Menarik secara ekonomi (**High Investment Attractiveness**)
- Aman secara sosial (**Low Social Conflict**)

Kombinasi dua faktor ini menciptakan peluang proyek yang **berkelanjutan**, **menguntungkan**, dan **berisiko rendah**, sehingga layak menjadi prioritas dalam strategi transisi energi hijau nasional.

Kali ini kita melakukan :
- `merge()` antar dua dataset
- Struktur **dictionary** di Python
- Teknik **conditional filtering**

Berikut tahapan yang dilakukan:

1. **Gabungkan** `Economic_Dataset.xlsx` dan `Social_Dataset.xlsx` berdasarkan `Project_ID`
2. **Simpan hasil gabungan ke dictionary** dengan:
   - `Project_ID` sebagai key
   - `(Daya_Tarik_Investasi, Tingkat_Konflik)` sebagai tuple value
3. **Gunakan for loop dan if** untuk menyaring proyek yang memenuhi kriteria:
   - `Daya_Tarik_Investasi == "High"`
   - `Tingkat_Konflik == "Low"`

```python
# Gabungkan data ekonomi dan sosial
merged_df = pd.merge(econ_df, social_df, on="Project_ID")

# Buat dictionary dari hasil gabungan
project_dict = {
    row['Project_ID']: (
        str(row['Daya_Tarik_Investasi']).strip(), 
        str(row['Tingkat_Konflik']).strip()
    )
    for _, row in merged_df.iterrows()
}

# Filter proyek yang memenuhi dua kriteria
print("Projects with High Investment Attractiveness and Low Conflict:")
found = False
for project_id, (invest, conflict) in project_dict.items():
    if invest.lower().startswith("high") and conflict.lower().startswith("low"):
        print(project_id)
        found = True

if not found:
    print("Tidak ada proyek yang memenuhi kriteria.")
```

Hasil analisis menunjukkan Empat proyek berhasil diidentifikasi memenuhi dua kriteria utama:

1. PLTM-SUMUT-001
2. PLTS-JATIM-001
3. PLTS-NTB-001
4. PLTS-JABW-001

Melalui analisis ini, dapat disaring proyek-proyek yang berpotensi unggul secara ekonomi dan aman secara sosial, menjadi dasar bagi perencanaan proyek energi hijau yang lebih efisien, inklusif, dan berisiko rendah. Pendekatan berbasis data ini memperkuat keputusan investasi dan mendukung strategi nasional dalam menciptakan lingkungan yang kondusif untuk transisi energi berkelanjutan.

### 4.5 Total Investasi untuk Lokasi dengan Efisiensi Tinggi

Analisis ini bertujuan untuk menghitung **total biaya investasi** pada proyek-proyek energi yang memiliki **Efisiensi Lokasi tinggi**, dengan menggabungkan data dari:

- `Geospatial_Dataset.xlsx`
- `Financial_Dataset.xlsx`

Pendekatan ini digunakan untuk menilai proyek-proyek yang layak menjadi prioritas pendanaan berdasarkan efisiensi lokasi dari segi biaya, infrastruktur, dan kemudahan implementasi.

Efisiensi lokasi (`Efisiensi_Lokasi`) mengacu pada penilaian spasial terhadap:

- **Biaya logistik**
- **Akses terhadap infrastruktur pendukung**
- **Kemudahan implementasi proyek di lapangan**

Proyek yang berada di lokasi efisien cenderung:

- 🏗️ Lebih cepat dibangun  
- 📉 Memiliki risiko operasional lebih rendah  
- 💰 Lebih stabil secara biaya investasi

Analisis ini dirancang untuk melatih konsep:
- 📥 **Fungsi dengan parameter** (`def calculate_total_investment`)
- 🔁 **Perulangan dengan `for loop`**
- ➗ **Operasi aritmatika untuk penjumlahan**

Berikut tahapan lengkapnya:

1. **Gabungkan data geospasial dan keuangan** menggunakan `merge()` berdasarkan kolom `Project_ID`.
2. **Buat fungsi** `calculate_total_investment()` yang menerima:
   - Daftar Project_ID
   - Data hasil gabungan
3. **Gunakan `for loop`** untuk mencari proyek dengan `Efisiensi_Lokasi == "High"` dan menjumlahkan nilai `Investment_Cost`.
4. **Tampilkan hasil akhir** dalam satuan miliar rupiah.

```python
# Fungsi untuk menghitung total investasi proyek dengan lokasi efisien tinggi
def calculate_total_investment(project_ids, merged_data):
    total = 0
    for project_id in project_ids:
        row = merged_data[merged_data["Project_ID"] == project_id]
        if not row.empty:
            lokasi = str(row["Efisiensi_Lokasi"].values[0]).strip().lower()
            if lokasi.startswith("high"):
                try:
                    investasi = float(row["Investment_Cost"].values[0])
                    total += investasi
                except ValueError:
                    print(f"Nilai investasi tidak valid untuk proyek: {project_id}")
    return total

# Ambil semua Project_ID dari data gabungan
project_ids = merged_df["Project_ID"].tolist()

# Hitung total investasi untuk proyek dengan efisiensi lokasi tinggi
total_investment = calculate_total_investment(project_ids, merged_df)

# Tampilkan hasilnya
print(f"Total Investment for High-Efficiency Locations: {total_investment:.2f} billion Rp")
```

Melalui analisis ini, diperoleh bahwa proyek-proyek dengan efisiensi lokasi tinggi telah menyerap total investasi sebesar Rp 955.73 miliar.
Temuan ini dapat digunakan sebagai dasar penyusunan prioritas pendanaan proyek energi terbarukan yang berbasis pada efisiensi dan kelayakan lokasi, mendukung transisi energi nasional yang lebih tepat sasaran.

