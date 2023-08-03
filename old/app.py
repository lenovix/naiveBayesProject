import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from NaiveBayes import NaiveBayes
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Membaca dataset dari file csv
df = pd.read_csv("emergency_dataset3.csv")

# Membagi dataset menjadi bagian pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(
    df["Text"], df["Unit"], test_size=0.3, random_state=42
)

# Membuat objek TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Mengonversi teks ke representasi TF-IDF
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Melatih model Naive Bayes dengan TF-IDF vectors
model = NaiveBayes()
model.fit(X_train_tfidf, y_train)


# Memprediksi kelas pada data pengujian
y_pred = model.predict(X_test_tfidf)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)

# Data baru yang ingin diprediksi
data = "Ada orang yang terjebak"
new_data = [data]

# Melakukan transformasi TF-IDF pada data baru
new_data_tfidf = vectorizer.transform(new_data)

# Melakukan prediksi dengan model yang telah dilatih
predictions = model.predict(new_data_tfidf)


# Menampilkan hasil prediksi
for data, prediction in zip(new_data, predictions):
    print("Text:", data)
    print("Predicted Unit:", prediction)
    print()
