# Tout le contenu du site est ici, les pages font juste l'afficher.
# Nouveau projet = un dico de plus dans PROJETS, pas besoin de toucher aux pages.

# mes infos perso (dico : une clé -> une valeur)
PROFIL = {
    "nom": "Tino Carré",
    "titre": "M1 student in Health Artificial Intelligence (Master SIA)",
    "ville": "Dijon, France",
    "email": "carretino3@gmail.com",
    "github": "https://github.com/Tino971",
    "linkedin": "https://www.linkedin.com/in/tino-carre-02756a226",
    # les parenthèses collent les morceaux de texte en une seule chaîne
    "bio": (
        "I am a first-year master's student at Université Bourgogne Europe, "
        "after a B.U.T. in Data Science at IUT Besançon-Vesoul. "
        "I like turning raw data into clear tools: dashboards, statistical reports "
        "and small Python applications. During my bachelor's degree I worked as a "
        "Data Analyst apprentice at Tournus Équipement. I am now strengthening my "
        "programming, algorithms and machine learning skills."
    ),
}

# compétence -> niveau sur 100
COMPETENCES = {
    "Python": 80,
    "SQL": 80,
    "Power BI": 85,
    "Excel / VBA": 85,
    "R": 70,
    "Statistics": 75,
    "Machine learning": 55,
}

PROJETS = [
    {
        "titre": "Tic-tac-toe with tkinter",
        "desc": "A tic-tac-toe game against a computer that wins when it can, "
                "blocks the player otherwise, then takes the centre. "
                "Game logic and window are in separate, tested files.",
        "tags": ["Python", "GUI", "Algorithms"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": None,
    },
    {
        "titre": "Moving a character on a grid",
        "desc": "A 4 x 4 tkinter grid where a character moves cell by cell "
                "around walls. Clicks, distances and neighbours are pure "
                "functions checked by unit tests.",
        "tags": ["Python", "GUI", "Testing"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": None,
    },
    {
        "titre": "Search benchmark: list, NumPy, binary search tree",
        "desc": "Measured the time needed to find a value in a Python list, "
                "a sorted NumPy array and a binary search tree, for sizes up "
                "to one million, and plotted the curves.",
        "tags": ["Python", "Algorithms", "Data"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": "assets/search_times.png",
    },
    {
        "titre": "Météo-France weather dashboard",
        "desc": "Interactive Power BI report on 70 years of Météo-France sensor "
                "data (1950-2022) for three departments: hot, rainy, stormy and "
                "foggy days, and a map of the sensors.",
        "tags": ["Power BI", "Data visualisation"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project1.jpg",
    },
    {
        "titre": "Air quality in Romainville",
        "desc": "Statistical report on fine particles (PM10, PM2.5, PM1): "
                "yearly, seasonal and daily variations, and links with "
                "temperature and humidity.",
        "tags": ["Statistics", "Data"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project2.jpg",
    },
    {
        "titre": "Parcoursup dashboard (team project)",
        "desc": "Power BI dashboard on the 2023 admissions of IUT Besançon-Vesoul: "
                "candidates, places, fill rate and profile of admitted students "
                "for each department. Team of four.",
        "tags": ["Power BI", "Data visualisation"],
        "annee": 2024,
        "lien": None,
        "image": "assets/project3.jpg",
    },
    {
        "titre": "First portfolio (HTML, Node.js, PostgreSQL)",
        "desc": "a Node.js/Express server, with a PostgreSQL database for the "
                "portfolio content.",
        "tags": ["HTML", "Node.js", "PostgreSQL"],
        "annee": 2024,
        "lien": "https://github.com/Tino971/portfolio",
        "image": "assets/project4.jpg",
    },
    {
        "titre": "Bachelor's degree competencies database",
        "desc": "a Node.js/Express server, with a PostgreSQL database for the "
                "competencies of my bachelor's degree.",
        "tags": ["Web", "SQL", "JavaScript"],
        "annee": 2025,
        "lien": None,
        "image": None,
    },
]

# mes études : (période, diplôme et école)
PARCOURS = [
    ("2026 - 2028", "Master SIA (M1 in progress), Université Bourgogne Europe, Dijon"),
    ("2023 - 2026", "B.U.T. Data Science (VCOD track), IUT Besançon-Vesoul, Dole campus"),
    ("2023", "French Baccalauréat (Mathematics, Advanced Mathematics, Engineering Science), "
             "Lycée Gabriel Voisin, Tournus"),
]

# mes jobs : (période, poste, boîte)
EXPERIENCES = [
    ("2025 - 2026", "Data Analyst (apprenticeship)", "Tournus Équipement"),
    ("Jul - Aug 2024", "Packaging operator", "Bourgogne Repas, Cuisery"),
    ("Aug 2023", "Campsite assistant: reception, bar, activities", "Camping Saint-Martin, Sorèze"),
    ("Jul 2023", "Packaging operator", "Bourgogne Repas, Cuisery"),
]

# langue -> niveau
LANGUES = {"French": "native", "English": "C1 (EF SET)", "Spanish": "B2"}

# simple liste de mots
LOISIRS = ["Rugby", "Cooking", "Music", "Travel"]
