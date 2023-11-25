# Laporan Proyek Stroke Prediction

Disusun oleh: Aditya Atallah

## Domain Proyek
### Latar Belakang
Stroke merupakan masalah kesehatan utama bagi masyarakat modern. Hal tersebut dikarenakan serangan stroke yang mendadak dapat mengakibatkan kematian, kecacatan fisik dan mental baik pada usia produktif maupun usia lanjut [1] Efek stroke bergantung pada bagian otak mana yang terluka dan seberapa parah pengaruhnya. Kematian secara mendadak dapat terjadi ketika seorang pasien mengalami stroke yang sangat parah (WHO, 2014). [2]

Penyakit stroke dapat terjadi karena beberapa faktor, diantaranya tekanan darah, riwayat fibrilasi atrium, kolesterol, diabetes dan lain sebagainya. Selama ini penanganan penyakit stroke dilakukan secara manual, dimana pasien melakukan pemeriksaan pada dokter spesialis penyakit syaraf. [2]

Dengan adanya faktor-faktor penyebab terjadinya stroke, dibutuhkanlah sebuah alat yang dapat mendeteksi seseorang dapat terindikasi dapat terkena stroke atau tidak. Sebagai contoh, aplikasi atau alat kedokteran yang dilengkapi dengan algoritma machine learning dapat menjadi solusi efektif. Algoritma ini dapat diprogram untuk menganalisis data kesehatan pasien, seperti riwayat tekanan darah, kadar kolesterol, dan faktor risiko lainnya. Melalui pendekatan machine learning, algoritma ini dapat belajar dari pola-pola yang kompleks dan memberikan prediksi yang akurat terkait kemungkinan pasien terkena stroke.

Penerapan _Machine Learning_ pada bidang Kesehatan bukanlah hal baru, telah banyak penerapan yang dilakukan, sebagai contoh: alat Pendeteksi Penyakit melalui Citra medis seperti _CT Scan_, _MRI_. alat ini menggunakan machine learning untuk mendeteksi atau mendiagnosis penyakit. Misalnya, diagnosis kanker paru-paru, penyakit jantung, penyakit hati, dan lain sebagainya.

Pada proyek ini model prediksi stroke menggunakan data kegiatan dan informasi pribadi pasien yang dilakukan seperti, tipe perkejaan, married atau tidak, memiliki tekanan darah tinggi atau tidak dan lainnya dalam memprediksi seseorang kemungkinan memiliki stroke atau tidak.

Dengan adanya sebuah model prediksi stroke ini, Sistem ini akan membantu pihak yang berwenang dalam hal ini rumah sakit dan dokter untuk melakukan pencegahan dini terhadap pasien yang memiliki kemungkinan terkena stroke 


##  Business Undestanding
### Problem Statement
- Fitur apa saja yang paling mempengaruhi seseorang terkena stroke atau tidak?
- Bagaimana cara menghasilkan data yang baik digunakan untuk model _Machine Learning_?
- Seberapa akurat hasil klasifikasi stroke dengan fitur yang digunakan?

### Goals
- Mengetahui fitur yang paling mempengaruhi dapat menyebabkan stroke
- Membangun sistem yang dapat mengumpulkan dan mengelola data kesehatan pasien dengan aman dan efektif, termasuk data kegiatan dan informasi pribadi yang relevan untuk prediksi stroke.
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

|       | Age    | avg_glucose_level | bmi  |
|-------|--------|-------------------|------|
|count  | 5110   |51110              | 4909 |
|mean   | 43.215 | 106.147           | 28.8 |
| std   | 22.633 | 45.28             | 7.85 |
|min    | 0      | 55.12             | 10.3 |
| 25%   | 25     | 77.245            | 23.5 |
| 50%   | 45     | 91.885            | 28.1 |
| 75%   | 61     | 114.09            | 33.1 |
| max   | 82     | 271.74            | 97.6 |

### Univariate Analysis
#### Categorical Feature
 - Feature Gender
    |Sample | Pria   | Wanita | Others | 
    |-------|--------|--------|--------|
    |Gender | 2513   |1701    | 1      |
Terdapat 1 nilai error yaitu Others, maka nilai tersebut akan dihapus.


    
  - Pada Setiap Feature berikut ini yaitu hypertension, heart_disease, ever_merried, work_type, Residence_type dan smoking_status tidak terjadi nilai error, akan tetapi penyebaran data tiap feature tidak merata yang mungkin dapat menyebabkan bias
     - Hypertension
          |Sample | 0  | 1 |  
          |-------|--------|--------|
          |Hypertension| 3923 |292     |

       
      - Heart_disease
          |Sample | 0  | 1 |  
          |-------|--------|--------|
          |Heart_disease| 4060 |155     |

      - Ever_married
          |Sample | Yes  | No |  
          |-------|--------|--------|
          |Ever_married| 2642 |1573     |

      - Work_type
          |Sample | Private | Self-Employed | Children  |Govt_job | Never_worked |
          |-------|--------|--------|---|-------|--------|
          |Work_type | 2412 |629     | 620 | 532  | 22 |

      - Resident_type
          |Sample | Urban  | Rural |  
          |-------|--------|--------|
          |Resident_type| 2138 |2077     |
        
      - smoking_status
          |Sample | never_smoked |unknown |formly_smoked  |smokes |
          |-------|--------|--------|--|--|
          |Smoking_status| 1569 |1339     | 671  |636 |
  
  
#### Numerical Features
- Penyebaran data untuk feature BMI dan Age cukup normal akan tetapi tidak pada feature Avg_glucosa_lvl yang cenderung miring ke kanan
- pada feature age rata-rata umur pada dataset ini adalah 40 hingga 50
- pada feature BMI rata-rata berat ideal seseorang berada di 25-30
- pada feature Avg_glucosa_level rata-rata berada disekiatar 70-100 akan tetapi banyak juga yang mencapai lebih dari 160 untuk tingkat gula darah


<div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/b368125b-fae0-4a25-951d-9e0db0c4f4d0"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

### Multivariet Analysis
#### Categorical Feature
- Feature Gender
    feature gender tidak memiliki korelasi terhadap penyebab stroke, karena baik pria dan wanita dapat terkena stroke
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/43957849-98d7-498a-a56f-0f4485d910c1"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>
 
- Feature Hypertension
    feature Hypertension memiliki korelasi penyebab stroke jika seseorang memiliki hypertensi maka ada kemungkinan terkena stroke
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
    feature ever Married memilikki pengaruh terjadinya stroke, berdarkan data seseorang yang telah menikah cenderung dapat terkena stroke dibandingkan dengan yang tidak menikah
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/78f85712-aa9e-4ece-876a-b6119c400903"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature Work_type
    Feature work type memiliki pengaruh terhadap terjadinya seseorang stroke, ketika seseorang memiliki pekerjaan tertentu dapat menyebabkan stroke dibandingkan yang tidak bekerja, hal ini dapat dipengaruhi berbagai hal seperti tekanan ditempat kerja jadwal pekerjaan yang padat dan banyak hal lain
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/351acae8-c508-429b-a555-f8a700a596e5"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature Residance type
    feature residance type tidak terlalu mempengaruhi seseorang terjadinya stroke atau tidak, baik tinggal didaerah perkotaan ataupun pedesaan
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/0a26744d-979c-4279-82c8-1c97a48bd8e3"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

- Feature smoking_status
    feature smoking status tidak terlalu memiliki korelasi terjadinya stroke. pada data baik yang tidak merokok, maupun yang merokok dapat terkena stroke
  <div>
    <img src="https://github.com/ahdithya/stroke-prediction/assets/91508590/09ad6dba-6fc0-49cc-b541-40db1a5afe12"  style='display: block;
    margin-left: auto;
    margin-right: auto;'/>
  </div><br>

#### Numerical Feature
Korelasi antar numeric feature, tidak memiliki hubungan satu sama lain, hal ini dapat diliat dari nilai tiap korealsi yang berada disekitar nol koma.
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
    _K-Nearest Neighbors_ (KNN) adalah algoritma yang digunakan untuk masalah klasifikasi dan regresi. algoritma ini bekerja dengan cara mengklasifikasikan suatu data berdasarkan mayoritas kelas dari _k-nearest neighbors_ (tetangga terdekat) di sekitarnya. Jika suatu data memiliki mayoritas tetangga dari kelas A, maka data tersebut diklasifikasikan sebagai kelas A.
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
    _Support Vector Machine_ (SVM) adalah algoritma machine learning yang digunakan untuk masalah klasifikasi dan regresi.  _SVM_ berusaha menemukan batas keputusan (_decision boundary_) yang optimal untuk memisahkan dua kelas. Batas keputusan ini ditemukan dengan mencari _hyperplane_ yang memiliki margin terbesar antara dua kelas. 
    - Kelebihan
        Efektif di Ruang Dimensi Tinggi terutama ketika jumlah fitur (variabel) lebih besar dari jumlah sampel.
        Mampu Menangani Data yang Tidak Terpisah Linear: Dengan menggunakan kernel yang sesuai, SVM dapat menangani data yang tidak dapat dipisahkan secara linear.
        Tahan terhadap Overfitting: SVM memiliki kemampuan untuk mengontrol overfitting melalui parameter 
    - Kekurangan
        Pemilihan Kernel yang Tidak Tepat: Pemilihan kernel yang tidak tepat dapat menghasilkan performa model yang buruk.
        Komputasi yang Intensif: _SVM_ dapat menjadi komputasi yang intensif, terutama jika datasetnya besar.
        Tidak Cocok untuk Dataset Besar: _SVM_ mungkin kurang cocok untuk dataset yang sangat besar karena memerlukan memori dan waktu komputasi yang signifikan.
    - parameter
        - `C`: Parameter yang mengontrol trade-off antara margin dan kesalahan klasifikasi.
        - `kernel`: Jenis kernel yang akan digunakan (linear, polynomial, radial basis function (RBF), dll.).
        - `gamma`: Koefisien kernel untuk 'rbf', 'poly', dan 'sigmoid'. Nilai yang tinggi akan menghasilkan margin yang lebih rendah dan lebih kompleks.
- Random Forest Classifer
    _Random Forest_ adalah algoritma _ensemble_ yang digunakan untuk masalah klasifikasi dan regresi. Ensemble learning melibatkan penggabungan hasil beberapa model untuk meningkatkan kinerja dan ketahanan model terhadap overfitting. Random Forest mengoperasikan sekelompok pohon keputusan yang dihasilkan secara acak dan menggabungkan hasil prediksi mereka.
    - Kelebihan
        Kinerja yang Tinggi: Random Forest cenderung memberikan kinerja yang tinggi karena menggabungkan prediksi dari beberapa pohon keputusan.
        Ketahanan terhadap _Overfitting_: Dengan membangun pohon keputusan dari subset acak fitur dan sampel, Random Forest lebih tahan terhadap overfitting dibandingkan dengan pohon keputusan tunggal.
        Kemampuan Menangani Data yang Tidak Seimbang: _Random Forest_ dapat menangani ketidakseimbangan kelas dengan memberikan bobot yang seimbang pada setiap pohon.
    - Kekurangan
        Interpretasi yang Sulit: Random Forest umumnya sulit untuk diinterpretasi, terutama ketika terdiri dari banyak pohon.
        Komputasi yang Intensif: Pelatihan Random Forest dapat menjadi komputasi yang intensif terutama pada dataset besar dan dengan jumlah pohon yang tinggi.
    - parameter
        - `n_estimators`: Jumlah pohon dalam ensemble.
        - `max_depth`: Kedalaman maksimum setiap pohon.
        - `min_samples_split`: Jumlah sampel minimum yang diperlukan untuk membagi simpul internal.
        - `min_samples_leaf`: Jumlah sampel minimum yang diperlukan untuk menjadi daun (simpul paling bawah).
         
- Hyperparameter Tuning
    _Hyperparameter tuning_ adalah proses mencari kombinasi optimal dari hyperparameter untuk suatu model machine learning dengan tujuan meningkatkan performa model. Menentukan hyperparameter yang optimal dapat membantu meningkatkan kinerja model dan mengurangi risiko _overfitting_ atau _underfitting_. pada proyek menggunakan GridSearch dalam mencari parameter yang telah ditentukan
  - _K-Neighbors Classifer_
    Parameter:
    - `n_neighbors` : 4
  - _Random Forest Classifer_
    - `n_estimators`: 50
    - `max_depth`: None
    - `min_samples_split`: 2
    - `min_samples_leaf`: 1
  - _Support Vector Machine Classifer_
    - `C`: 0.1
    - `kernel`: 'linear
    - `gamma`: 0.1
   
  
Dari Hasil Model dan Hyperparamter Tuning yang digunakan, Algoritma terbaik yang dapat digunakan adalah _Random Forest_ 

## Evaluasi 
_Accuracy score_ adalah suatu metrik evaluasi yang umum digunakan dalam masalah klasifikasi untuk mengukur sejauh mana model klasifikasi dapat membuat prediksi yang benar. Metrik ini mengukur persentase jumlah prediksi yang tepat dibandingkan dengan jumlah total sampel.
img

 Dalam Klasifikasi Biner, jumlah prediksi benar dapat dihitung sebagai jumlah _True Positives (TP)_ dan _True Negatives (TN)_, sedangkan jumlah total sampel adalah jumlah seluruh sampel (termasuk _False Positives_ dan _False Negatives_).
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

dari Hasil Evaluasi _Accuracy Score_ tampak setiap model menunjukan hasil yang baik yaitu diatas 95%, akan tetapi jika diliat lebih detail _Random Forest_ memiliki hasil Evaluasi yang paling tinggi dibanding model lainnya


Hasil Pengujian:

5 data pertama pada data test
|  y_true | prediksi_knn  | prediksi_svm  | prediksi_rfc   |   
|---------|---------------|---------------|----------------|
| 0       |             0 |            0  |             0  |   
|       0 |             0 |            0  |    0           |   
|  0      |             0 |            0  |              0 |   
|  0      |             0 |            0  |              0 |   
|  0      |             0 |            0  |              0 | 


Pada pengujian data test, semua mengklasifikasikan data test dengan benar dimana hasil y_true adalah 0 yang artinya tidak terkena stroke dan hasil prediksi tiap model juga menunjukan angka 0 yang artinya sesuai dengan hasil sebenarnya. sehingga setiap model mampu memprediksi seseorang terkena stroke atau tidak. akan tetapi disini akan menggunakan model _Random Forest Classifier_ sebagai model utama dikarenakan tingkat akurasi yang diberikan lebih tinggi dibanding model lainnya.


## Kesimpulan
Model _Machine Learning_ yang dihasilkan dapat secara tepat memprediksi seseorang terkan stroke atau tidak. hal ini dapat membantu pengembangan pada bidang medis dengan menggunakan _machine learning_ untuk mempermudah melakukan tindak pencegahan ketika pasien memiliki tanda-tanda stroke atau tidak


REFERENCE :

[1] Teknika, J., & Estian Pambudi, R. (n.d.). Teknika 16 (02): 221-226. IJCCS, x, No.x, 1–5.
[2] Puspitawuri, A., Santoso, E., & Dewi, C. (2019). Diagnosis Tingkat Risiko Penyakit Stroke Menggunakan Metode K-Nearest Neighbor dan Naïve Bayes (Vol. 3, Issue 4). http://j-ptiik.ub.ac.id

