import numpy as np


class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.num_classes = len(self.classes)
        self.num_features = X.shape[1]
        self.priors = np.zeros(self.num_classes)
        self.likelihoods = np.zeros((self.num_classes, self.num_features))

        # Menghitung priors (probabilitas kelas)
        for i, c in enumerate(self.classes):
            self.priors[i] = np.sum(y == c) / len(y)

        # Menghitung likelihoods (probabilitas atribut)
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.likelihoods[i] = (np.sum(X_c, axis=0) + 1) / (
                np.sum(X_c) + self.num_features
            )

    def predict(self, X):
        preds = []

        # Memprediksi kelas untuk setiap data uji
        for x in X:
            posteriors = []

            # Menghitung posteriors (probabilitas kelas | data uji) untuk setiap kelas
            for i, c in enumerate(self.classes):
                likelihood = np.sum(
                    np.log(self.likelihoods[i][x.indices])
                )  # Menggunakan indeks bulat pada matriks sparse
                posterior = np.log(self.priors[i]) + likelihood
                posteriors.append(posterior)

            # Memilih kelas dengan posterior tertinggi sebagai prediksi
            pred = self.classes[np.argmax(posteriors)]
            preds.append(pred)

        return preds
