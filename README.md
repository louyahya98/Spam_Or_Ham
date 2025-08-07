
# 📧 Système Intelligent de Filtrage des Emails pour la Sécurité des Communications

Ce projet utilise le Machine Learning pour détecter et classifier les emails comme **spam** ou **ham (non-spam)**. Il propose une interface utilisateur simple via **Streamlit**, permettant de tester le modèle en temps réel.

## 🧠 Objectif

Protéger les utilisateurs des emails indésirables et potentiellement dangereux en classifiant automatiquement les messages entrants à l'aide d'un modèle SVM entraîné sur des données textuelles.

---

## 📁 Structure du projet

```
📦 spam-filter-streamlit/
├── model.pkl               # Modèle entraîné (LinearSVC)
├── vectorizer.pkl          # TF-IDF vectorizer entraîné
├── app.py                  # Application Streamlit principale
├── data/
│   └── spam_dataset.csv    # Dataset utilisé pour l'entraînement (facultatif)
├── README.md               # Fichier de documentation
```

---

## ⚙️ Technologies utilisées

- Python 3.x
- Scikit-learn (`LinearSVC`, `TfidfVectorizer`)
- Streamlit
- Pandas
- Pickle

---

## 🚀 Instructions d’exécution

### 1. Installer les dépendances

Assure-toi d’avoir Python 3.8+ installé.

Installe les packages nécessaires :
```bash
pip install streamlit scikit-learn pandas
```

### 2. Lancer l’application Streamlit

```bash
streamlit run app.py
```

Cela ouvrira l’application dans ton navigateur par défaut.

---

## 💻 Fonctionnalités

- Interface **en français**
- Zone de texte pour tester un email
- Prédiction affichée : "Spam" ou "Ham"
- Classifieur basé sur `LinearSVC` avec `TfidfVectorizer`

---

## 🔐 Sécurité

Ce projet est un prototype à but pédagogique. Pour un usage réel :
- Ajouter une base de données pour stocker les logs / emails
- Mettre en place une couche d’authentification
- Élargir les filtres à d’autres types d’attaques (phishing, malware)

---

## 📌 Auteur

Projet réalisé par [Ton Nom], 2025.

---

## 📜 Licence

MIT – Vous êtes libre de l'utiliser, modifier et distribuer.
