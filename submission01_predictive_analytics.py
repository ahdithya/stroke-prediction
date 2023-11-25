# -*- coding: utf-8 -*-
"""submission01-predictive_analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZS_mPucjT_07Sd1HqvP0TzXP87D6g0eA

# Stroke Prediction

Oleh: Aditya Atallah

dataset : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
"""

# Commented out IPython magic to ensure Python compatibility.
# memanggil library yang digunakan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

"""## Data Collection"""

# mengimport dataset
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.head()

# melihat ukuran data
df.shape

"""Data memiliki 5110 baris data dan 12 column"""

# melihat informasi data
df.info()

"""**Variable Informasi**

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

"""

# Menghapus feature yang tidak digunakan yaitu column id
df.drop(columns='id', inplace=True)
df.columns.to_list()

# mengubah data types
df['age'] = df['age'].astype('int')
df['hypertension'] = df['hypertension'].astype('object')
df['Residence_type'] = df['Residence_type'].astype('object')
df['heart_disease'] = df['heart_disease'].astype('object')
df['stroke'] = df['stroke'].astype('object')

df.dtypes

# melihat deskripsi statistik pada data
df.describe()

"""### Missing Value"""

# pada feature Age terdapat nilai 0, sedangkan tidak ada seseorang yang berumur 0
df = df[df['age'] != 0]
print(df.shape)

# melakukan pengecekan Missing Value
df.isna().sum()

"""pada column bmi terdapat data yang hilang sebesar 201. Pada tahapan ini akan melakukan untuk mengatasinya melakukan penghapusan pada data yang missing"""

# menghapus missing value
df.dropna(axis=0,inplace=True)
df.shape

# mengecek data yang duplikat
duplicated = df.duplicated().sum()
print(f'Data yang duplikat berjumlah : {duplicated}')

"""### Outliers"""

num_features = ['age', 'bmi', 'avg_glucose_level']

plt.figure(figsize=(12, 6))
for i, col in enumerate(num_features, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(y=df[col])
    plt.title(f'Box Plot of {col}')
    plt.ylabel(col)


plt.tight_layout()
plt.show()

"""Terdapat Outliers pada feature BMI dan Avg_glucose_level, untuk mengatasi akan melakukan penghapusan pada nilai outlier"""

# menghapus outliers
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
IQR = q3 - q1


df = df[~((df<(q1-1.5*IQR))|(df>(q3+1.5*IQR))).any(axis=1)]

df.shape

"""## Exploratory Data Analysis

### Univariate Analysis
"""

numerical_features = ['age','avg_glucose_level','bmi']
categorical_features = ['gender','hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status', 'stroke']

df.info()

"""#### Categorical Features"""

for feature in categorical_features:
    count = df[feature].value_counts()
    percent = 100 * df[feature].value_counts(normalize=True)
    features = pd.DataFrame({'jumlah sampel': count, 'persentase': percent.round(1)})
    print(f"\nStatistik untuk feature: {feature}\n{features}")
    count.plot(kind='bar', title=feature)
    plt.show()
    print('\n')

"""
pada feature gender terdapat nilai error yaitu dimana gender bernilai other, untuk itu akan melakukan penghapusan data pada feature gender yang bernilai other"""

# menghapus nilai error
df= df[df['gender']!='Other']
x = df.gender.value_counts()
print(x)

"""#### Numerical Features"""

df.hist(bins=50, figsize=(20,15))
plt.show()

"""pada column age dan bmi distribusi data cukup normal akan tetapi pada avg_glucose_level data miring kekanan yang mana akan berdampak pada model

### Multivariate Analysis

#### Categorical Features
"""

cat_features = df.select_dtypes(include = 'object').columns.to_list()

for col in cat_features:
  if col != 'stroke':
    sns.catplot(data=df, x=col, y='stroke', kind='bar', dodge=False, height=4, aspect=3, palette='Set3')
    plt.title("Rata-rata 'stroke' Relatif terhadap - {}".format(col))

"""#### Numerical Features"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5 )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""korelasi antar feature menunjukan arah positif, tidak ada feature yang memiliki yang sangat tinggi

## Data Preprocessing

#### One Hot Encoding Feature Categorical
"""

df = pd.get_dummies(df, columns=['hypertension','heart_disease','gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'], drop_first=True)
df['stroke'] = df['stroke'].astype('int')
df.head()

"""#### Train-Test Split"""

from sklearn.model_selection import train_test_split

X = df.drop(columns='stroke')
y = df['stroke']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, shuffle=True
)

print(f'Data Train')

"""#### Standarisasi"""

# melakukan Standarisasi pada data numerik tidak pada one-hot encoding
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df[numerical_features])
X_train[numerical_features] = scaler.transform(X_train[numerical_features])
X_train[numerical_features].head()

"""## Modelling"""

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit

"""#### Hyperparameter Tuning"""

models = {
    'knn': KNeighborsClassifier(),
    'svc': SVC(),
    'rfc': RandomForestClassifier()
}

params_grid = {
    'knn': {
        'n_neighbors': [3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    },
    'svc': {
         'C': [0.1, 1, 10],
         'kernel': ['linear', 'rbf'],
         'gamma': [0.1, 1, 10]
    },
    'rfc': {
         'n_estimators': [50, 100, 200],
         'max_depth': [None, 10, 20],
         'min_samples_split': [2, 5, 10],
         'min_samples_leaf': [1, 2, 4]
    }
}

scores = []
# cross-validation
cv = ShuffleSplit(n_splits=5, test_size=0.05, random_state=123)


for key, value in models.items():
  params = params_grid[key]
  gridSearch = GridSearchCV(value, params, cv=cv, return_train_score=False)
  gridSearch.fit(X_train, y_train)
  scores.append({
        'model': key,
        'best_score': gridSearch.best_score_,
        'best_params': gridSearch.best_params_
    })
result = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])

result

"""#### Modelling with Best Parameter"""

# Model KNN
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
knn_acc= knn.score(X_train,y_train)

# Model SVC
svc = SVC(C=0.1, gamma=0.1, kernel='linear')
svc.fit(X_train, y_train)
svc_acc = svc.score(X_train, y_train)

# Model Random Forest Classifier
rfc = RandomForestClassifier(max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=50)
rfc.fit(X_train, y_train)
rfc_acc= rfc.score(X_train, y_train)

# Hasil model pada data train
result_model = pd.DataFrame({
    'Model': ['SVM', 'Random Forest', 'KNN'],
    'Accuracy': [svc_acc, rfc_acc, knn_acc]
})
result_model

"""Hasil akurasi model terbaik yaitu Random Forest Classifier

## Evaluation
"""

from sklearn.metrics import accuracy_score

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

acc_score = pd.DataFrame(
    columns=['Train', 'Test'],
    index=['SVC', 'KNN', 'RFC']
)

model_dict = {'KNN': knn, 'RFC': rfc, 'SVC': svc}

for name, model in model_dict.items():
    acc_score.loc[name, 'Train'] = accuracy_score(y_true=y_train, y_pred=model.predict(X_train))
    acc_score.loc[name, 'Test'] = accuracy_score(y_true=y_test, y_pred=model.predict(X_test))

acc_score

fig, ax = plt.subplots()
acc_score.sort_values(by='Test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Secara keseluruhan setiap model menghasilkan Accuracy score yang sangat tinggi yaitu sekitar 0.97 dan pada data test memiliki hasil akurasi yang sama yaitu 0.97"""

prediksi = X_test.iloc[0:5].copy()
pred_dict = {'y_true':y_test[30:35]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)