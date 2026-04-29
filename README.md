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
student-dropout-prediction/
│
├── model.joblib
├── scaler.joblib
├── notebook.ipynb
├── app.py
├── README.md
├── insight_dt_dicoding-dashboard.jpg
├── metabase.db.mv.db
└── requirements.txt
```

**Setup environment - Anaconda**
1. Buka terminal
2. Jalankan perintah berikut untuk membuat environment.
   ```
   conda create --name dropout-env python=3.12
   ```
4. Aktifkan virtual environment.
   ```
   conda activate dropout-env
   ```
5. Pindah ke direktori project
   ```
   D:
   cd student-dropout-prediction
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
- **Username**: insight.dt@gmail.com
- **Password**: data404

#### Cara Menjalankan
1. Pastikan Docker sudah terinstall pada perangkat Anda.
2. Jalankan Metabase menggunakan perintah berikut:
   ```
   docker run -d -p 3000:3000 -v D:\student-dropout-prediction:/metabase.db --name metabase metabase/metabase
   ```
4. Buka browser dan akses:
   ```
   http://localhost:3000
   ```
5. Login menggunakan username dan password yang telah disediakan.
6. Setelah berhasil masuk, pada halaman utama pilih menu **Our analytics**.
7. Masuk ke dalam koleksi tersebut, lalu scroll ke bawah hingga menemukan dashboard bernama **Dropout Risk Dashboard**.
8. Klik pada dashboard tersebut.
9. Setelah itu, dashboard akan terbuka dan menampilkan seluruh visualisasi analisis Dropout Risk.

## Menjalankan Sistem Machine Learning
**Demo Aplikasi**

Prototipe sistem machine learning dapat diakses melalui link berikut: [Student Dropout Prediction App](https://student-dropout-prediction.streamlit.app)

**Cara Menjalankan Secara Lokal**
1. Bukan terminal anaconda
2. Kemudian setup environment anaconda 
3. Masuk ke Folder Project
4. Jalankan Aplikasi Streamlit
   ```
   streamlit run app.py
   ```
   Biarkan kolom email kosong, lalu tekan Enter.
5. Akses Aplikasi di Browser
   ```
   http://localhost:8501
   ```
6. Cara Menggunakan Aplikasi
   Setelah aplikasi terbuka:
   - Masukkan data mahasiswa pada form input (kolom kiri)
   - klik tombol “Predict”
   - Hasil akan muncul di kolom kanan berupa:
     - Status risiko dropout
     - Probabilitas risiko
     - Insight Sederhana
     


## Conclusion
Berdasarkan hasil analisis eksploratif data (EDA) dan visualisasi melalui dashboard, ditemukan bahwa faktor utama yang berkaitan dengan risiko dropout mahasiswa adalah performa akademik, terutama pada semester kedua. Indikator seperti jumlah mata kuliah yang diselesaikan (curricular units approved) dan nilai pada semester kedua memiliki pengaruh paling besar terhadap status mahasiswa. Selain faktor akademik, faktor finansial seperti status pembayaran biaya kuliah dan kondisi sebagai debtor juga turut berpengaruh, meskipun tidak sekuat faktor akademik. Sementara itu, nilai saat masuk dan latar belakang akademik sebelumnya memiliki kontribusi yang relatif lebih kecil dalam menjelaskan kemungkinan dropout. Dashboard yang dikembangkan juga berhasil menyajikan informasi secara terstruktur mulai dari gambaran umum data, distribusi status mahasiswa, hingga faktor-faktor utama yang memengaruhi dropout, sehingga membantu dalam memahami pola data secara lebih jelas.

Dari sisi model machine learning, hasil evaluasi menunjukkan performa yang cukup baik dengan accuracy sebesar 0.88. Model mampu mengklasifikasikan mahasiswa pada kelas Dropout dan Graduate dengan nilai precision dan recall yang seimbang, yaitu precision 0.88 dan recall 0.80 untuk kelas Dropout, serta recall 0.94 untuk kelas Graduate. Secara keseluruhan, F1-score berada pada rentang 0.84 hingga 0.91 yang menunjukkan keseimbangan performa model. Berdasarkan feature importance, variabel yang paling berpengaruh dalam prediksi adalah jumlah dan nilai mata kuliah yang diselesaikan pada semester pertama dan kedua, khususnya curricular_units_2nd_sem_approved, curricular_units_1st_sem_approved, dan curricular_units_2nd_sem_grade, diikuti oleh faktor finansial seperti status pembayaran biaya kuliah. Hal ini memperkuat hasil EDA bahwa performa akademik merupakan faktor paling dominan dalam menentukan risiko dropout mahasiswa.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan institut guna menyelesaikan permasalahan mereka.
- Intervensi Akademik Dini
  Institusi perlu melakukan pemantauan performa akademik mahasiswa sejak semester awal, khususnya pada nilai dan jumlah mata kuliah yang diselesaikan, untuk mengidentifikasi mahasiswa berisiko dan memberikan bimbingan akademik secara tepat waktu.
- Dukungan Finansial Terarah
  Institusi disarankan untuk memberikan perhatian khusus kepada mahasiswa dengan kendala pembayaran, seperti melalui skema bantuan finansial atau pengaturan ulang pembayaran, guna mengurangi risiko dropout yang disebabkan oleh faktor ekonomi.
