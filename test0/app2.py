import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Membaca dataset dari file csv
df = pd.read_csv("emergency_dataset3.csv")

# Membagi dataset menjadi bagian pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(
    df["Text"], df["Unit"], test_size=0.3, random_state=42
)

# Membuat objek TF-IDF vectorizer
vectorizer = TfidfVectorizer(min_df=1)

# Mengonversi teks ke representasi TF-IDF
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("vectorize: ", vectorizer.get_feature_names_out())

# Melatih model Naive Bayes dengan TF-IDF vectors
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Memprediksi kelas pada data pengujian
y_pred = model.predict(X_test_tfidf)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)

# Data baru yang ingin diprediksi
data = ["saat sesak nafas", "disini ada orang yang sesak nafas"]
new_data = data

# Melakukan transformasi TF-IDF pada data baru
new_data_tfidf = vectorizer.transform(new_data)
print("new_data_tfidf: ", new_data_tfidf)

# Melakukan prediksi dengan model yang telah dilatih
predictions = model.predict(new_data_tfidf)

# Mengambil kata kunci dari variabel new_data
keywords = vectorizer.inverse_transform(new_data_tfidf)[0]
print("Kata Kunci:", keywords)

# Menampilkan hasil prediksi
for data, prediction in zip(new_data, predictions):
    print("Text:", data)
    print("Predicted Unit:", prediction)
    print()
