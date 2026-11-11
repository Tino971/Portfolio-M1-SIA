PROFIL = {
    "nom": "Tino Carré",
    "titre": "Étudiant en M1 Santé et Intelligence Artificielle (Master SIA)",
    "ville": "Dijon, France",
    "email": "carretino3@gmail.com",
    "github": "https://github.com/Tino971",
    "linkedin": "https://www.linkedin.com/in/tino-carre-02756a226",
    "bio": (
        "Je suis en première année de master à l'Université Bourgogne Europe, "
        "après un B.U.T. Science des Données à l'IUT Besançon-Vesoul. "
        "J'aime transformer des données brutes en outils clairs : tableaux de bord, "
        "rapports statistiques et petites applications Python. Pendant mon B.U.T., "
        "j'ai été Data Analyst en alternance chez Tournus Équipement pendant deux ans, "
        "où j'ai travaillé avec des données SAP, Excel/VBA et Python. Aujourd'hui, "
        "je progresse en programmation, en algorithmique et en machine learning."
    ),
}

COMPETENCES = {
    "Python": 80,
    "SQL": 80,
    "Power BI": 85,
    "Excel / VBA": 85,
    "R": 70,
    "Statistiques": 75,
    "Machine learning": 55,
}

ALTERNANCE = {
    "titre": "Alternance Data Analyst - Tournus Équipement (2024 - 2026)",
    "texte": (
        "Tournus Équipement fabrique du matériel en inox pour les cuisines professionnelles. "
        "J'étais dans les équipes Qualité et Marketing. Mon travail consistait surtout à "
        "extraire des données de SAP HANA, à les nettoyer et à créer des outils Excel/VBA "
        "pour générer des documents."
    ),
    "image": "assets/projets/alternance.jpg",
    "pdf": "assets/pdf/alternance_tournus.pdf",
}

PROJETS = [
    {
        "titre": "Données produits pour un PIM",
        "desc": "Préparation des données d'environ 12 000 produits avant leur import "
                "dans un PIM : fusion de plusieurs sources, complétion des valeurs "
                "manquantes et rédaction de noms courts en français, anglais et allemand.",
        "tags": ["SQL", "Power Query", "Qualité des données"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/pim.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Fiches environnementales produits",
        "desc": "Outil Excel/VBA qui récupère la nomenclature d'un produit dans SAP "
                "et calcule sa recyclabilité et son CO2, pondérés par le poids de "
                "chaque pièce. La fiche est ensuite enregistrée en PDF.",
        "tags": ["SQL", "Excel / VBA", "Automatisation"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/environnement.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Reporting des KPI commerciaux",
        "desc": "Automatisation des indicateurs commerciaux mensuels (chiffre d'affaires, "
                "12 mois glissants, écart au budget, marge) à partir d'exports SAP, "
                "sur quatre ans de commandes et de factures.",
        "tags": ["SQL", "Power Query", "Excel / VBA", "Python"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/kpi.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Certificats de conformité",
        "desc": "Création d'une table reliant produits et normes, puis de macros VBA "
                "qui génèrent les certificats de deux marques en français, anglais "
                "et allemand.",
        "tags": ["Excel / VBA", "Automatisation"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/certificats.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Base de pièces détachées",
        "desc": "Nettoyage et fusion d'environ 1 000 pièces détachées réparties dans "
                "plusieurs fichiers, traduction des noms manquants avec l'API DeepL "
                "en Python, et génération de fiches pour le service après-vente.",
        "tags": ["Python", "SQL", "Qualité des données"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/sav.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Enquête sur l'éco-anxiété à Dole",
        "desc": "Enquête pour la ville de Dole auprès de 169 lycéens et étudiants. "
                "J'ai construit le score d'éco-anxiété, fait les corrélations sous R "
                "et réalisé les slides Power BI. Équipe de cinq.",
        "tags": ["Statistiques", "R", "Power BI"],
        "annee": 2024,
        "lien": None,
        "image": "assets/projets/dole.png",
        "pdf": "assets/pdf/eco_anxiete_dole.pdf",
    },
    {
        "titre": "Morpion avec tkinter",
        "desc": "Un morpion contre un ordinateur qui gagne quand il peut, "
                "bloque le joueur sinon, puis prend le centre. "
                "La logique du jeu et la fenêtre sont dans des fichiers séparés et testés.",
        "tags": ["Python", "Interface graphique", "Algorithmique"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": None,
        "pdf": None,
    },
    {
        "titre": "Déplacer un personnage sur une grille",
        "desc": "Une grille tkinter de 4 x 4 où un personnage se déplace case par case "
                "en contournant des murs. Les clics, les distances et les voisins sont "
                "des fonctions pures vérifiées par des tests unitaires.",
        "tags": ["Python", "Interface graphique", "Tests"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": None,
        "pdf": None,
    },
    {
        "titre": "Comparaison de recherche : liste, NumPy, arbre binaire de recherche",
        "desc": "Mesure du temps nécessaire pour trouver une valeur dans une liste Python, "
                "un tableau NumPy trié et un arbre binaire de recherche, pour des tailles "
                "allant jusqu'à un million, avec les courbes associées.",
        "tags": ["Python", "Algorithmique", "Données"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": "assets/search_times.png",
        "pdf": None,
    },
    {
        "titre": "Tableau de bord météo Météo-France",
        "desc": "Rapport Power BI interactif sur 70 ans de données des capteurs "
                "Météo-France (1950-2022) pour trois départements : jours chauds, "
                "pluvieux, orageux et de brouillard, et carte des capteurs.",
        "tags": ["Power BI", "Visualisation de données"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project1.jpg",
        "pdf": None,
    },
    {
        "titre": "Qualité de l'air à Romainville",
        "desc": "Rapport statistique sur les particules fines (PM10, PM2.5, PM1) : "
                "variations annuelles, saisonnières et journalières, et liens avec "
                "la température et l'humidité.",
        "tags": ["Statistiques", "Données"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project2.jpg",
        "pdf": None,
    },
    {
        "titre": "Tableau de bord Parcoursup (projet d'équipe)",
        "desc": "Tableau de bord Power BI sur les admissions 2023 de l'IUT Besançon-Vesoul : "
                "candidats, places, taux de remplissage et profil des admis "
                "pour chaque département. Équipe de quatre.",
        "tags": ["Power BI", "Visualisation de données"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project3.jpg",
        "pdf": None,
    },
    {
        "titre": "Premier portfolio (HTML, Node.js, PostgreSQL)",
        "desc": "Mon premier site portfolio, avec un serveur Node.js/Express et une "
                "base de données PostgreSQL pour le contenu.",
        "tags": ["HTML", "Node.js", "PostgreSQL"],
        "annee": 2024,
        "lien": "https://github.com/Tino971/portfolio",
        "image": "assets/project4.jpg",
        "pdf": None,
    },
    {
        "titre": "Base de données des compétences du B.U.T.",
        "desc": "Un serveur Node.js/Express avec une base de données PostgreSQL "
                "pour les compétences de mon B.U.T.",
        "tags": ["Web", "SQL", "JavaScript"],
        "annee": 2025,
        "lien": None,
        "image": None,
        "pdf": None,
    },
]

PARCOURS = [
    ("2026 - 2028", "Master SIA (M1 en cours), Université Bourgogne Europe, Dijon"),
    ("2023 - 2026", "B.U.T. Science des Données (parcours VCOD), IUT Besançon-Vesoul, site de Dole"),
    ("2023", "Baccalauréat général (Mathématiques, Mathématiques expertes, Sciences de l'ingénieur), "
             "Lycée Gabriel Voisin, Tournus"),
]

EXPERIENCES = [
    ("2024 - 2026", "Data Analyst (alternance)", "Tournus Équipement"),
    ("Juil. - août 2024", "Opérateur de conditionnement", "Bourgogne Repas, Cuisery"),
    ("Août 2023", "Employé de camping : accueil, bar, animations", "Camping Saint-Martin, Sorèze"),
    ("Juil. 2023", "Opérateur de conditionnement", "Bourgogne Repas, Cuisery"),
]

LANGUES = {"Français": "langue maternelle", "Anglais": "C1 (EF SET)", "Espagnol": "B2"}

LOISIRS = ["Rugby", "Cuisine", "Musique", "Voyages"]
