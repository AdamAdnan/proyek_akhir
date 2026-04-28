# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam menghasilkan lulusan berkualitas. Namun demikian, institusi ini masih menghadapi tantangan berupa tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout), yang dapat berdampak pada reputasi institusi, efisiensi operasional, serta kualitas pendidikan secara keseluruhan. Oleh karena itu, diperlukan pendekatan berbasis data untuk mengidentifikasi mahasiswa yang berpotensi mengalami dropout sejak dini, sehingga institusi dapat melakukan intervensi yang lebih tepat sasaran dan efektif. Sistem yang dikembangkan diharapkan dapat berfungsi sebagai early warning system dalam mendukung pengambilan keputusan berbasis data.

### Permasalahan Bisnis
Berdasarkan kondisi tersebut, permasalahan bisnis yang dihadapi adalah sebagai berikut:

1. Tidak adanya sistem deteksi dini untuk mengidentifikasi mahasiswa yang berpotensi dropout.
2. Kurangnya pemahaman berbasis data terkait faktor-faktor yang memengaruhi terjadinya dropout.
3. Monitoring performa mahasiswa belum optimal karena data yang tersedia belum diolah menjadi informasi yang informatif dan mudah dipahami.
4. Intervensi yang dilakukan belum tepat sasaran karena belum berbasis pada tingkat risiko masing-masing mahasiswa.

### Cakupan Proyek
Proyek ini bertujuan untuk mengatasi permasalahan dropout dengan mengembangkan sistem berbasis machine learning yang mampu melakukan deteksi dini terhadap mahasiswa berisiko. Model prediksi akan dibangun dengan mengeksplorasi dan membandingkan berbagai algoritma machine learning untuk memperoleh model dengan performa terbaik. Selain itu, akan dilakukan analisis terhadap fitur-fitur penting guna mengidentifikasi faktor utama yang berkontribusi terhadap risiko dropout. Sebagai implementasi, proyek ini juga mencakup pengembangan prototipe sistem prediksi sederhana yang dapat digunakan oleh pihak institusi, serta dashboard interaktif yang menyajikan informasi performa mahasiswa dan tingkat risiko dropout secara komprehensif untuk mendukung proses monitoring dan pengambilan keputusan.

Berdasarkan cakupan proyek tersebut, diperlukan beberapa resource dan tools sebagai berikut:
- Dataset mahasiswa yang mencakup informasi akademik, demografi, serta kondisi sosial-ekonomi.
- Bahasa pemrograman Python sebagai tools utama dalam pengolahan data dan pengembangan model.
- Berbagai library pendukung untuk analisis data dan pengembangan model machine learning.
- Streamlit sebagai tools untuk membangun prototipe sistem prediksi sederhana.
- Metabase sebagai tools untuk mengembangkan dashboard interaktif.

### Persiapan

Sumber data: [Students' performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Struktur Folder**
```
employee-attrition-analytics/
│
├── model.pkl
├── features.pkl
├── notebook.ipynb
├── prediction.py
├── README.md
├── insight_dt_dicoding-dashboard.jpg
├── insight_dt_dicoding-video
├── metabase.db.mv.db
└── requirements.txt
```

**Setup environment - Anaconda**
1. Buka terminal
2. Jalankan perintah berikut untuk membuat environment.
   ```
   conda create --name employee-dashboard python=3.12
   ```
4. Aktifkan virtual environment.
   ```
   conda activate employee-dashboard
   ```
5. Pindah ke direktori project
   ```
   D:
   cd employee-attrition-analytics
   ```
6. Instal semua library yang dibutuhkan menggunakan perintah berikut.
   ```
   pip install -r requirements.txt
   ```

## Business Dashboard
Dashboard **Dropout Risk Dashboard** dirancang untuk membantu institusi dalam memantau kondisi mahasiswa dan mengidentifikasi risiko dropout secara dini berbasis data. Dashboard ini menyajikan ringkasan utama seperti jumlah mahasiswa, tingkat dropout, dan kelulusan, serta distribusi tingkat risiko mahasiswa untuk mendukung deteksi awal. Analisis menunjukkan bahwa faktor akademik, seperti nilai dan jumlah unit yang diselesaikan, memiliki pengaruh paling besar terhadap risiko dropout, sementara faktor finansial seperti status pembayaran juga berkontribusi sebagai faktor pendukung. Selain itu, dashboard ini menyediakan rekomendasi tindakan yang dapat digunakan untuk menentukan intervensi yang tepat, sehingga membantu institusi dalam mengurangi tingkat dropout secara lebih efektif.

### Akses Dashboard Metabase

#### Informasi Akses
- **Metabase Version**: 0.59.5.1
- **Database File**: `metabase.db.mv.db`
- **Username**: admin123@gmail.com
- **Password**: admin123

#### Cara Menjalankan
1. Pastikan Docker sudah terinstall pada perangkat Anda.
2. Jalankan Metabase menggunakan perintah berikut:
   ```
   docker run -d -p 3000:3000 -v D:\employee-attrition-analytics:/metabase.db --name metabase metabase/metabase
   ```
4. Buka browser dan akses:
   ```
   http://localhost:3000
   ```
5. Login menggunakan username dan password yang telah disediakan.
6. Setelah berhasil masuk, pada halaman utama pilih menu **Our analytics**.
7. Masuk ke dalam koleksi tersebut, lalu scroll ke bawah hingga menemukan dashboard bernama **HR Attrition Analytics Dashboard**.
8. Klik pada dashboard tersebut.
9. Setelah itu, dashboard akan terbuka dan menampilkan seluruh visualisasi analisis HR Attrition.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
