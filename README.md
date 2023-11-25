# Laporan Proyek Stroke Prediction

Disusun oleh: Aditya Atallah

## Domain Proyek
### Latar Belakang
Stroke merupakan masalah kesehatan utama bagi masyarakat modern. Hal tersebut dikarenakan serangan stroke yang mendadak dapat mengakibatkan kematian, kecacatan fisik dan mental baik pada usia produktif maupun usia lanjut [1] Efek stroke bergantung pada bagian otak mana yang terluka dan seberapa parah pengaruhnya. Kematian secara mendadak dapat terjadi ketika seorang pasien mengalami stroke yang sangat parah (WHO, 2014). [2]

Penyakit stroke dapat terjadi karena beberapa faktor, diantaranya tekanan darah, riwayat fibrilasi atrium, kolesterol, diabetes dan lain sebagainya. Selama ini penanganan penyakit stroke dilakukan secara manual, dimana pasien melakukan pemeriksaan pada dokter spesialis penyakit syaraf. [2]

Dengan adanya faktor-faktor penyebab terjadinya stroke, dibutuhkanlah sebuah alat yang dapat mendeteksi seseorang dapat terindikasi dapat terkena stroke atau tidak. Melalui Pendekatan machine learning hal itu dapat dicapai sehingga dapat mengetahui seseorang dapat terkena stroke atau tidak.

Dengan adanya sebuah model prediksi stroke ini, ini akan membantu pihak yang berwenang dalam hal ini rumah sakit dan dokter untuk melakukan pencegahan dini terhadap pasien yang memiliki kemungkinan terkena stroke 

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
- Membuat Model Machine Learning yang dapat mengklasifikasikan seseorang terkena stroke secara akurat yaitu dengan memiliki tingkat akurasi 95%

### Solution Statements
- Menggunakan beberapa algoritma machine learning, dalam proyek ini akan menggunakan Random Forest, KNN dan Suport Vector Machine (SVM).
- Melakukan _Hyperparameter tuning_ untuk meningkatkan akurasi model.
- Melakukan Matrik evaluasi untuk mengevaluasi seberapa baik model dalam memprediksi


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
  margin-right: auto;'/>
</div><br>

### Univariate Analysis
#### Categorical Feature
 - Feature Gender
   <div>
  <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/b26a415d-ffbf-4295-9733-5d4a061e00a0"  style='display: block;
  margin-left: auto;
  margin-right: auto;'/>
</div><br>
Terdapat 1 nilai error yaitu Others, maka nilai tersebut akan dihapus.


    
  - Pada Setiap Feature selanjutnya tidak terjadi nilai error, akan tetapi penyebaran data tiap feature tidak merata yang mungkin dapat menyebabkan bias
   img
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/881a8801-13a7-4b8d-9de5-045272811584"  style='display: block;
      margin-left: auto;
      margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/a54053a8-ade8-4981-84f3-b67ccd57368f"  style='display: block;
      margin-left: auto;
      margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/88601e8a-241a-4164-8c0e-389d00917e6f"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/06a7db76-5bf2-4adb-ba78-67d3728baa07"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/5bbd63e8-4758-4c32-9263-2f372c9f09d7"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/6bee6502-3968-4628-935e-a5ef670911a8"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/ca5de0d2-a71e-44d8-9e1b-724a00e251ec"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

  
#### Numerical Features
- Penyebaran data untuk feature BMI dan Age cukup normal akan tetapi tidak pada feature Avg_glucosa_lvl yang cenderung miring ke kanan


<div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/b368125b-fae0-4a25-951d-9e0db0c4f4d0"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

### Multivariet Analysis
#### Categorical Feature
- Feature Gender
    feature gender tidak memiliki korelasi terhadap penyebab stroke
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/43957849-98d7-498a-a56f-0f4485d910c1"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
 
- Feature Hypertension
    feature Hypertension memiliki korelasi penyebab stroke jika seseorang memiliki hypertensi
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/b299f367-b8c3-4495-b726-52ac77e5dade"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature Heart Disease
    feature Heart Disease memiliki pengaruh penyebab terjadi stroke jika seseorang memiliki heart disease
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/7f754b13-7de0-48ee-9374-f55955949a70"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature ever Married
    feature ever Married memilikki pengaruh terjadinya stroke
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/78f85712-aa9e-4ece-876a-b6119c400903"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature Work_type
    Feature work type memiliki pengaruh terhadap terjadinya seseorang stroke
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/351acae8-c508-429b-a555-f8a700a596e5"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature Residance type
    feature residance type tidak terlalu mempengaruhi seseorang terjadinya stroke atau tidak
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/0a26744d-979c-4279-82c8-1c97a48bd8e3"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature smoking_status
    feature smoking status memiliki pengaruh seseorang terkan stroke atau tidak
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/09ad6dba-6fc0-49cc-b541-40db1a5afe12"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

#### Numerical Feature
Korelasi antar numeric feature, tidak memiliki hubungan satu sama lain
<div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/ce9d3a16-30d0-4f94-9826-a264729efa3f"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>


## Data Preparation
- One Hot Encoding
    One-Hot Encoding adalah teknik yang mengubah data kategorik menjadi data numeric. Setiapdata  kategori menjadi kolom baru dengan nilai 0 atau 1.  Hal ini  sangat berguna ketika memiliki data kategori yang tidak dapat langsung digunakan dalam model matematis. Pada proyek ini fitur yang akan melakukan one hot encoding adalah hypertension,heart_disease,gender, ever_married, work_type, Residence_type, smoking_status
- Train-Test Split
    Melakukan Train-Test Split menjadi 2 kelompok data yaitu data Train yang digunakan untuk melatih model dan data test untuk melakukan pengujian setelah model dilatih. Hal ini dilakukan untuk menghasilkan model yang dapat memprediksi pada data yang belum pernah dilihat sebelumnya. pada proyek ini data dibagi menjadi 80% data train dan 20% data test
- Standarization
    Standarization adalah  proses yang dilakukan pada data numerik dalam analisis statistik dan machine learning untuk mengubah distribusi data sehingga memiliki rata-rata 0 dan deviasi standar 1. hal ini dilakukan untuk menyamakan scala data tanpa kehilangan nilai data yang sebenarnya


## Modelling
Pada Proyek ini menggunakan 3 Algoritma yaitu K-Neighbors Classifer, Support Vector Machine Classifer dan Random Forest Classifier
- K-Neighbors Classifer
    K-Nearest Neighbors (KNN) adalah algoritma yang digunakan untuk masalah klasifikasi dan regresi. algoritma ini bekerja dengan cara mengklasifikasikan suatu data berdasarkan mayoritas kelas dari k-nearest neighbors (tetangga terdekat) di sekitarnya. Jika suatu data memiliki mayoritas tetangga dari kelas A, maka data tersebut diklasifikasikan sebagai kelas A.
    - Kelebihan
        Sederhana dan Mudah Dimengerti
        Tidak Memerlukan Training Modelnya langsung menggunakan data pelatihan untuk melakukan prediksi.
        Kemampuan Menangani Data Nonlinear dan Multikelas yaitu KNN mampu menangani masalah klasifikasi multikelas.
    - Kekurangan
        Komputasi yang Tinggi
        Sensitif terhadap Outlier
        Memerlukan Penyesuaian Parameter 
    - parameter 
        + `n_neighbors` : Menentukan jumlah tetangga terdekat yang akan dipertimbangkan
- Support Vector Machine Classifer
    Support Vector Machine (SVM) adalah algoritma machine learning yang digunakan untuk masalah klasifikasi dan regresi.  SVM berusaha menemukan batas keputusan (decision boundary) yang optimal untuk memisahkan dua kelas. Batas keputusan ini ditemukan dengan mencari hyperplane yang memiliki margin terbesar antara dua kelas. 
    - Kelebihan
        Efektif di Ruang Dimensi Tinggi terutama ketika jumlah fitur (variabel) lebih besar dari jumlah sampel.
        Mampu Menangani Data yang Tidak Terpisah Linear: Dengan menggunakan kernel yang sesuai, SVM dapat menangani data yang tidak dapat dipisahkan secara linear.
        Tahan terhadap Overfitting: SVM memiliki kemampuan untuk mengontrol overfitting melalui parameter 
    - Kekurangan
        Pemilihan Kernel yang Tidak Tepat: Pemilihan kernel yang tidak tepat dapat menghasilkan performa model yang buruk.
        Komputasi yang Intensif: SVM dapat menjadi komputasi yang intensif, terutama jika datasetnya besar.
        Tidak Cocok untuk Dataset Besar: SVM mungkin kurang cocok untuk dataset yang sangat besar karena memerlukan memori dan waktu komputasi yang signifikan.
    - parameter
        - `C`: Parameter yang mengontrol trade-off antara margin dan kesalahan klasifikasi.
        - `kernel`: Jenis kernel yang akan digunakan (linear, polynomial, radial basis function (RBF), dll.).
        - `gamma`: Koefisien kernel untuk 'rbf', 'poly', dan 'sigmoid'. Nilai yang tinggi akan menghasilkan margin yang lebih rendah dan lebih kompleks.
- Random Forest Classifer
    Random Forest adalah algoritma ensemble yang digunakan untuk masalah klasifikasi dan regresi. Ensemble learning melibatkan penggabungan hasil beberapa model untuk meningkatkan kinerja dan ketahanan model terhadap overfitting. Random Forest mengoperasikan sekelompok pohon keputusan yang dihasilkan secara acak dan menggabungkan hasil prediksi mereka.
    - Kelebihan
        Kinerja yang Tinggi: Random Forest cenderung memberikan kinerja yang tinggi karena menggabungkan prediksi dari beberapa pohon keputusan.
        Ketahanan terhadap Overfitting: Dengan membangun pohon keputusan dari subset acak fitur dan sampel, Random Forest lebih tahan terhadap overfitting dibandingkan dengan pohon keputusan tunggal.
        Kemampuan Menangani Data yang Tidak Seimbang: Random Forest dapat menangani ketidakseimbangan kelas dengan memberikan bobot yang seimbang pada setiap pohon.
    - Kekurangan
        Interpretasi yang Sulit: Random Forest umumnya sulit untuk diinterpretasi, terutama ketika terdiri dari banyak pohon.
        Komputasi yang Intensif: Pelatihan Random Forest dapat menjadi komputasi yang intensif terutama pada dataset besar dan dengan jumlah pohon yang tinggi.
    - parameter
        - `n_estimators`: Jumlah pohon dalam ensemble.
        - `max_depth`: Kedalaman maksimum setiap pohon.
        - `min_samples_split`: Jumlah sampel minimum yang diperlukan untuk membagi simpul internal.
        - `min_samples_leaf`: Jumlah sampel minimum yang diperlukan untuk menjadi daun (simpul paling bawah).
         
- Hyperparameter Tuning
    Hyperparameter tuning adalah proses mencari kombinasi optimal dari hyperparameter untuk suatu model machine learning dengan tujuan meningkatkan performa model. Menentukan hyperparameter yang optimal dapat membantu meningkatkan kinerja model dan mengurangi risiko overfitting atau underfitting. pada proyek menggunakan GridSearch dalam mencari parameter yang telah ditentukan
  - K-Neighbors Classifer
    Parameter:
    - `n_neighbors` : 4
  - Random Forest Classifer
    - `n_estimators`: 50
    - `max_depth`: None
    - `min_samples_split`: 2
    - `min_samples_leaf`: 1
  - Support Vector Machine Classifer
    - `C`: 0.1
    - `kernel`: 'linear
    - `gamma`: 0.1
   
  
Dari Hasil Model dan Hyperparamter Tuning yang digunakan, Algoritma terbaik yang dapat digunakan adalah Random Forest 

## Evaluasi 
Accuracy score adalah suatu metrik evaluasi yang umum digunakan dalam masalah klasifikasi untuk mengukur sejauh mana model klasifikasi dapat membuat prediksi yang benar. Metrik ini mengukur persentase jumlah prediksi yang tepat dibandingkan dengan jumlah total sampel.
img

 Dalam Klasifikasi Biner, jumlah prediksi benar dapat dihitung sebagai jumlah True Positives (TP) dan True Negatives (TN), sedangkan jumlah total sampel adalah jumlah seluruh sampel (termasuk False Positives dan False Negatives).
<div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/d5d112cb-2c56-40f1-8f51-096106947d16"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
<div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/a1621729-91d1-4d09-b397-4d4feb25be45"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

 Hasil Evlauasi Proyek :
 - Accuracy

|      | Train        | Test     |
|------|--------------|----------|
| SVC  |  0.969149	  | 0.96204  |  
|  KNN |  0.968852    | 0.959668 |  
|  RFC |  0.999703	  | 0.96204  |  

 - Acurracy Score
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/c96b44ae-2fc8-402d-a5e2-0c16447da3d2"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
  Gambar Hasil Akurasi score dimana semakin mendekati 1 hasil model semakin bagus akurasi model tersebut.

dari Hasil Evaluasi Accuracy Score tampak setiap model menunjukan hasil yang baik yaitu diatas 95%, akan tetapi jika diliat lebih detail Randome Forest memiliki hasil Evaluasi yang paling tinggi dibanding model lainnya


Hasil Pengujian:
5 data pertama pada data test
|  y_true | prediksi_knn  | prediksi_svm  | prediksi_rfc   |   
|---------|---------------|---------------|----------------|
| 0       |             0 |            0  |             0  |   
|       0 |             0 |            0  |    0           |   
|  0      |             0 |            0  |              0 |   
|  0      |             0 |            0  |              0 |   
|  0      |             0 |            0  |              0 | 


Pada pengujian data test, semua mengklasifikasikan data test dengan benar dimana hasil y_true adalah 0 yang artinya tidak terkena stroke dan hasil prediksi tiap model juga menunjukan angka 0 yang artinya sesuai dengan hasil sebenarnya. sehingga setiap model mampu memprediksi seseorang terkena stroke atau tidak. akan tetapi disini akan menggunakan model Random Forest Classifier sebagai model utama dikarenakan tingkat akurasi yang diberikan lebih tinggi dibanding model lainnya.


## Kesimpulan
Model Machine Learning yang dihasilkan dapat secara tepat memprediksi seseorang terkan stroke atau tidak. hal ini dapat membantu pengembangan pada bidang medis dengan menggunakan machine learning untuk mempermudah melakukan tindak pencegahan ketika pasien memiliki tanda-tanda stroke atau tidak


REFERENCE :

[1] Teknika, J., & Estian Pambudi, R. (n.d.). Teknika 16 (02): 221-226. IJCCS, x, No.x, 1–5.

[2] Puspitawuri, A., Santoso, E., & Dewi, C. (2019). Diagnosis Tingkat Risiko Penyakit Stroke Menggunakan Metode K-Nearest Neighbor dan Naïve Bayes (Vol. 3, Issue 4). http://j-ptiik.ub.ac.id

