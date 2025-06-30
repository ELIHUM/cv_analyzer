Analyseur de candidatures avec IA



Ce projet est une mini-application d’IA qui prédit si un profil est adapté à un poste, à partir d’un texte de CV.



--------------------------------------------------------------------------------------

Fonctionnalités

\- Traitement automatique de texte (TF-IDF)

\- Modèle de régression logistique

\- Interface web interactive avec Streamlit

-------------------------------------------------------------------------------------

Structure

\- `data.csv` : exemples de candidatures annotées

\- `model\_cv.py` : script d'entraînement

\- `app\_cv.py` : interface web Streamlit



Exécution

-------------------------------------------------------------------------------------

```bash

pip install -r requirements.txt

python model\_cv.py

streamlit run app\_cv.py



