import streamlit as st
import pickle

# Charger le modèle
with open("model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

st.title("🧠 Analyse de candidature")

texte = st.text_area("Collez ici le texte de la candidature (CV, profil, etc.)")

if st.button("Analyser"):
    vect = vectorizer.transform([texte])
    prediction = model.predict(vect)[0]
    prob = model.predict_proba(vect)[0][1]

    if prediction == 1:
        st.success(f"✅ Ce profil est adapté. (Probabilité : {prob:.2f})")
    else:
        st.error(f"❌ Ce profil n'est **pas adapté**. (Probabilité : {prob:.2f})")
