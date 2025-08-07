# app.py

import streamlit as st
import pickle

# Charger le modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Charger le vectoriseur
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Configuration de la page
st.set_page_config(page_title="Détecteur de SPAM", layout="centered")

# Interface utilisateur
st.title("📧 Détection de SPAM / HAM")
st.markdown("Cette application permet de détecter si un email est **spam** ou **non spam (ham)** à l'aide d'un modèle Machine Learning.")

# Zone de saisie
email_input = st.text_area("✉️ Entrez l'email à analyser :", height=200)

# Bouton
if st.button("Analyser"):
    if not email_input.strip():
        st.warning("⚠️ Veuillez entrer un texte d'email.")
    else:
        # Vectoriser le texte
        X_input = vectorizer.transform([email_input])
        prediction = model.predict(X_input)[0]

        # Affichage du résultat
        if prediction == 1:
            st.error("🔴 Résultat : SPAM détecté !")
        else:
            st.success("🟢 Résultat : Email sain (HAM)")
