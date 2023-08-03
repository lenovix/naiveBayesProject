from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from NaiveBayes import NaiveBayes
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Membaca dataset dari file csv
df = pd.read_csv("emergency_dataset.csv")

# Membagi dataset menjadi bagian pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(
    df["Text"], df["Unit"], test_size=0.3, random_state=42
)

# Membuat objek TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Mengonversi teks ke representasi TF-IDF
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
print(vectorizer.get_feature_names_out())

# Melatih model Naive Bayes dengan TF-IDF vectors
model = NaiveBayes()
model.fit(X_train_tfidf, y_train)

# Memprediksi kelas pada data pengujian
y_pred = model.predict(X_test_tfidf)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    new_texts = data.get("texts", [])

    print("data: ", data)
    print("new_texts: ", new_texts)

    # Transformasi data baru ke representasi vektor
    new_X = vectorizer.transform(new_texts)
    print("new_X: ", new_X)

    # Melakukan prediksi
    predictions = model.predict(new_X)
    print("predictions: ", predictions)

    # mengambil kata kunci
    keywords = vectorizer.inverse_transform(new_X)[0]
    print("Kata Kunci:", keywords)

    # Mengembalikan hasil prediksi
    results = [
        {"text": text, "prediction": prediction}
        for text, prediction in zip(new_texts, predictions)
    ]

    return jsonify(results)


if __name__ == "__main__":
    ipHP = "192.168.43.108"
    ip = "192.168.1.7"
    app.run(host=ipHP, port=5000)
