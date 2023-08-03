import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
dataset = pd.read_csv("dataset.csv")

# Split dataset into features (X) and target (y)
X = dataset["Text"]
y = dataset[["Ambulance", "Police", "Firefighter"]]

# Vectorize the text data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the Naive Bayes classifier for each target class
clf_ambulance = MultinomialNB()
clf_ambulance.fit(X_vectorized, y["Ambulance"])

clf_police = MultinomialNB()
clf_police.fit(X_vectorized, y["Police"])

clf_firefighter = MultinomialNB()
clf_firefighter.fit(X_vectorized, y["Firefighter"])

# Get input from the user
user_input = input("Masukkan keadaan darurat: ")

# Vectorize the user input
user_input_vectorized = vectorizer.transform([user_input])

# Predict the required units for each target class
prediction_ambulance = clf_ambulance.predict(user_input_vectorized)
prediction_police = clf_police.predict(user_input_vectorized)
prediction_firefighter = clf_firefighter.predict(user_input_vectorized)

# Print the predicted units
predicted_units = []
if prediction_ambulance:
    predicted_units.append("Ambulance")
if prediction_police:
    predicted_units.append("Police")
if prediction_firefighter:
    predicted_units.append("Firefighter")

print("Unit yang dibutuhkan: ", ", ".join(predicted_units))
