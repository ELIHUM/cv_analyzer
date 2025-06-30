import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Charger les données
df = pd.read_csv("data.csv")

# Séparer X et y
X = df["texte"]
y = df["label"]

# Vectorisation TF-IDF
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Modèle de classification
model = LogisticRegression()
model.fit(X_vect, y)

# Sauvegarder le modèle et le vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Modèle entraîné et sauvegardé avec succès.")
