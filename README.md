# Portfolio-M1-SIA

Site portfolio personnel réalisé en Python avec Streamlit - M1 SIA, Université Bourgogne Europe.

## Pages

- **À propos** : courte présentation et mon alternance chez Tournus Équipement
- **Projets** : mes projets, avec recherche, filtre par tag, tri par année et rapports PDF
- **Compétences** : niveau de mes compétences avec un graphique, ma formation et mes expériences
- **Contact** : un formulaire qui vérifie les champs et enregistre les messages dans `messages.csv`

## Lancer le site en local

Il faut Python 3.10 ou plus récent.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Le site s'ouvre ensuite sur http://localhost:8501.

## Organisation des fichiers

```
app.py           # point d'entrée : configuration, barre latérale et navigation
data.py          # tout le contenu (profil, compétences, projets)
composants.py    # affichage (lecteur de PDF)
outils.py        # logique : filtrer/chercher les projets, vérifier et enregistrer les messages
style.css        # style personnalisé
pages/           # un fichier par page
assets/          # images et PDF
```

Pour modifier les textes du site, il suffit de modifier `data.py`.
