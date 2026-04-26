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
#### Struktur Folder
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

#### Setup environment - Anaconda
```
conda create --name employee-dashboard python=3.12
conda activate employee-dashboard
D: 
cd employee-attrition-analytics
pip install -r requirements.txt
```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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
