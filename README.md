# 📊 Segmentation des clients télécom

Application **Streamlit** qui classe un client d'un opérateur télécom dans un
segment à partir de son comportement d'usage (appels, SMS, durée
d'abonnement, montant facturé, valeur client, etc.). Le modèle retenu est un
**DBSCAN** (clustering basé sur la densité), entraîné et exploré dans le
notebook associé, qui propose également un déploiement Gradio.

## Structure du projet

```
.
├── app.py                                              # Application Streamlit (interface + inférence)
├── requirements.txt                                    # Dépendances Python
├── data/
│   └── Customer_dataset.csv                            # Jeu de données brut utilisé pour l'entraînement
├── models/
│   └── modele_dbscan.joblib                            # Modèle DBSCAN entraîné (points cœurs, labels, eps, etc.)
├── outils/
│   └── utils.py                                        # Fonctions utilitaires
└── Customer_Segmentation_avec_deploiement_Gradio.ipynb  # Exploration, préparation des données et entraînement des modèles
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer l'application

```bash
streamlit run app.py
```

L'application permet de :

- Sélectionner des valeurs médianes ou l'un des exemples prédéfinis pour
  pré-remplir le formulaire.
- Saisir les caractéristiques d'un client.
- Obtenir son segment prédit, ou un avertissement si le client est atypique
  (point considéré comme une anomalie par DBSCAN).

## Entraînement du modèle

Le notebook `Customer_Segmentation_avec_deploiement_Gradio.ipynb` contient le
pipeline de préparation des données :

1. Analyse exploratoire (distributions, corrélations).
2. Normalisation des variables numériques.
3. Comparaison de plusieurs algorithmes de clustering (K-Means, DBSCAN).
4. Sélection du modèle DBSCAN, export des points cœurs, labels et paramètres
   (`eps`, valeurs par défaut, exemples) avec `joblib` dans `models/`.

## Jeu de données

`data/Customer_dataset.csv` contient 3150 lignes avec les colonnes
suivantes :

| Colonne                     | Description                                   |
|-------------------------------|-----------------------------------------------|
| `Call Failure`                | Nombre d'appels échoués                       |
| `Complains`                   | Présence de réclamations (0/1)                |
| `Subscription Length`         | Durée de l'abonnement (mois)                  |
| `Charge Amount`                | Montant facturé (catégorie)                   |
| `Seconds of Use`               | Durée totale d'utilisation (secondes)         |
| `Frequency of use`             | Fréquence d'utilisation                       |
| `Frequency of SMS`             | Fréquence d'envoi de SMS                      |
| `Distinct Called Numbers`      | Nombre de numéros distincts appelés           |
| `Age Group`                    | Tranche d'âge                                 |
| `Status`                       | Statut du client (actif/non actif)            |
| `Age`                           | Âge du client                                 |
| `Customer Value`               | Valeur estimée du client                      |

## Déploiement

Cette application est conçue pour être déployée sur **Streamlit Community
Cloud** :

1. Pousser ce dépôt sur GitHub.
2. Aller sur [share.streamlit.io](https://share.streamlit.io), se connecter
   avec GitHub.
3. Cliquer sur **New app**, sélectionner le dépôt, la branche `main` et le
   fichier `app.py`.
4. Déployer : l'application sera accessible via une URL publique du type
   `https://<nom-app>.streamlit.app`.
