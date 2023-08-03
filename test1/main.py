import pandas as pd
from sklearn.cluster import KMeans

# Baca data keadaan darurat dari file CSV atau sumber data lainnya
data = pd.read_csv("data_keadaan_darurat.csv")

# Proses data untuk persiapan pemodelan
X = data.iloc[:, 1:].values

# Menentukan jumlah cluster menggunakan metode elbow
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Menampilkan plot elbow untuk menentukan jumlah cluster yang optimal
import matplotlib.pyplot as plt

plt.plot(range(1, 11), wcss)
plt.title("Metode Elbow")
plt.xlabel("Jumlah Cluster")
plt.ylabel("WCSS")
plt.show()

# Menerapkan algoritma K-Means dengan jumlah cluster yang optimal
kmeans = KMeans(n_clusters=3, init="k-means++", random_state=42)
kmeans.fit(X)

# Menambahkan kolom prediksi ke data asli
data["Unit"] = kmeans.predict(X)

# Menampilkan hasil prediksi
print(data[["Keadaan Darurat", "Unit"]])
