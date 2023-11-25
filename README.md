# Laporan Proyek Stroke Prediction

Disusun oleh: Aditya Atallah

## Domain Proyek
### Latar Belakang
Stroke merupakan masalah kesehatan utama bagi masyarakat modern. Hal tersebut dikarenakan serangan stroke yang mendadak dapat mengakibatkan kematian, kecacatan fisik dan mental baik pada usia produktif maupun usia lanjut. Efek stroke bergantung pada bagian otak mana yang terluka dan seberapa parah pengaruhnya. Kematian secara mendadak dapat terjadi ketika seorang pasien mengalami stroke yang sangat parah (WHO, 2014).

Penyakit stroke dapat terjadi karena beberapa faktor, diantaranya tekanan darah, riwayat fibrilasi atrium, kolesterol, diabetes dan lain sebagainya. Selama ini penanganan penyakit stroke dilakukan secara manual, dimana pasien melakukan pemeriksaan pada dokter spesialis penyakit syaraf.

Dengan adanya faktor-faktor penyebab terjadinya stroke, dibutuhkanlah sebuah alat yang dapat mendeteksi seseorang dapat terindikasi dapat terkena stroke atau tidak. Melalui Pendekatan machine learning hal itu dapat dicapai sehingga dapat mengetahui seseorang dapat terkena stroke atau tidak

Referensi
- [Klasifikasi Penyakit Stroke Menggunakan Algoritma Decision Tree C.45](https://jurnal.polsri.ac.id/index.php/teknika/article/view/4914)
- [Diagnosis Tingkat Risiko Penyakit Stroke Menggunakan Metode K-Nearest Neighbor dan Naïve Bayes](https://j-ptiik.ub.ac.id/index.php/j-ptiik/article/view/4916)

##  Business Undestanding
### Problem Statement
- Fitur apa saja yang mempengeruhi seseorang terkena stroke atau tidak?
- Bagaimana cara menghasilkan data yang baik digunakan untuk model _Machine Learning_?
- Seberapa akurat hasil klasifikasi stroke dengan fitur yang digunakan?

### Goals
- Mengetahui fitur yang dapat menyebabkan stroke
- Melakukan _Pre-processing_ data sebelum digunakan pada model
- Membuat Model Machine Learning yang dapat mengklasifikasikan seseorang terkena stroke atau tidak seakurat mungkin

### Solution Statements
- Menggunakan beberapa algoritma machine learning, dalam proyek ini akan menggunakan Random Forest, KNN dan Suport Vector Machine (SVM).
- Melakukan _Hyperparameter tuning_ untuk meningkatkan akurasi model.
- Melakukan Matrik evaluasi untuk mengevaluasi seberapa baik model dalam memprediksi/


## Data Understanding
Dataset yang digunakan adalah Dataset Stroke Prediction. Dataset ini digunakan untuk memprediksi kemungkinan seorang pasien terkena stroke berdasarkan parameter input seperti jenis kelamin, usia, berbagai penyakit, dan status merokok. Setiap baris dalam data memberikan informasi yang relevan tentang pasien.
Link Dataset: [Stroke Prediciion Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

### Informasi Dataset:
- Dataset dalam bentuk format csv (Comma Seperated Value)
- Dataset memiliki 5110 sample dan 12 fitur
- Dataset terdapat missing value

### Variable pada Dataset:
- id: unique identifier
- gender: jenis kelamin pasien "Male", "Female" or "Other"
- age: umur pasien
- hypertension: 0 jika pasien tidak memiliki tekanan darah tinggi dan 1 jika memiliki
- heart_disease: 0 jika pasien tidak memiliki sakit jantung dan 1 jika memiliki
- ever_married: status Menikah "No" or "Yes"
- work_type: tipe perkejaan pasien "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
- Residence_type: Tempat tinggal seorang pasien dipedasaan yaitu "Rural" atau di perkotaan "Urban"
- avg_glucose_level: rata-rata kadar gula darah dalam waktu tertentu
- bmi: ukuran body mass index pasien
- smoking_status: Status Merekok pasien "formerly smoked", "never smoked", "smokes" or "Unknown"*
- stroke: 1 jika pasien memiliki stroke atau 0 jika tidak

Pada features id akan dihapus karena tidak memiliki hubungan dalam melakukan prediksi seseorang stroke

### Hasil Statistik Data
Berikut Tampilan hasil Statistik Data pada feature bertipe numeric
<div>
  <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/bacaec0b-5cd0-4639-9cf6-43432d99426e"  style='display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;'/>
</div><br>


