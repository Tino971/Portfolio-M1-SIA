PROFIL = {
    "nom": "Tino Carré",
    "titre": "M1 student in Health Artificial Intelligence (Master SIA)",
    "ville": "Dijon, France",
    "email": "carretino3@gmail.com",
    "github": "https://github.com/Tino971",
    "linkedin": "https://www.linkedin.com/in/tino-carre-02756a226",
    "bio": (
        "I am a first-year master's student at Université Bourgogne Europe, "
        "after a B.U.T. in Data Science at IUT Besançon-Vesoul. "
        "I like turning raw data into clear tools: dashboards, statistical reports "
        "and small Python applications. During my bachelor's degree I was a "
        "Data Analyst apprentice at Tournus Équipement for two years, where I worked "
        "with SAP data, Excel/VBA and Python. I am now improving my programming, "
        "algorithms and machine learning skills."
    ),
}

COMPETENCES = {
    "Python": 80,
    "SQL": 80,
    "Power BI": 85,
    "Excel / VBA": 85,
    "R": 70,
    "Statistics": 75,
    "Machine learning": 55,
}

ALTERNANCE = {
    "titre": "Data Analyst apprenticeship - Tournus Équipement (2024 - 2026)",
    "texte": (
        "Tournus Équipement makes stainless-steel equipment for professional kitchens. "
        "I was in the Quality and Marketing teams. Most of my work was extracting data "
        "from SAP HANA, cleaning it, and building Excel/VBA tools to generate documents."
    ),
    "image": "assets/projets/alternance.jpg",
    "pdf": "assets/pdf/alternance_tournus.pdf",
}

PROJETS = [
    {
        "titre": "Product data for a PIM",
        "desc": "Prepared the product data of about 12,000 products before their "
                "import into a PIM: merged several sources, filled missing values "
                "and wrote short product names in French, English and German.",
        "tags": ["SQL", "Power Query", "Data quality"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/pim.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Environmental product sheets",
        "desc": "Excel/VBA tool that takes the bill of materials of a product from "
                "SAP and calculates its recyclability and CO2, weighted by the weight "
                "of each part. The sheet is then saved as a PDF.",
        "tags": ["SQL", "Excel / VBA", "Automation"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/environnement.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Sales KPI reporting",
        "desc": "Automated the monthly sales indicators (turnover, rolling 12 months, "
                "budget gap, margin) from SAP exports, on four years of orders "
                "and invoices.",
        "tags": ["SQL", "Power Query", "Excel / VBA", "Python"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/kpi.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Compliance certificates",
        "desc": "Made a table linking products and standards, then VBA macros that "
                "generate the certificates for two brands in French, English "
                "and German.",
        "tags": ["Excel / VBA", "Automation"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/certificats.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Spare parts database",
        "desc": "Cleaned and merged about 1,000 spare parts that were spread over "
                "several files, translated the missing names with the DeepL API "
                "in Python, and generated sheets for the after-sales service.",
        "tags": ["Python", "SQL", "Data quality"],
        "annee": 2026,
        "lien": None,
        "image": "assets/projets/sav.jpg",
        "pdf": "assets/pdf/alternance_tournus.pdf",
    },
    {
        "titre": "Eco-anxiety survey in Dole",
        "desc": "Survey for the city of Dole with 169 high-school and university "
                "students. I built the eco-anxiety score, did the correlations in R "
                "and made the Power BI slides. Team of five.",
        "tags": ["Statistics", "R", "Power BI"],
        "annee": 2024,
        "lien": None,
        "image": "assets/projets/dole.png",
        "pdf": "assets/pdf/eco_anxiete_dole.pdf",
    },
    {
        "titre": "Tic-tac-toe with tkinter",
        "desc": "A tic-tac-toe game against a computer that wins when it can, "
                "blocks the player otherwise, then takes the centre. "
                "Game logic and window are in separate, tested files.",
        "tags": ["Python", "GUI", "Algorithms"],
        "annee": 2026,
        "lien": "https://github.com/Tino971",
        "image": None,
        "pdf": None,
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
        "pdf": None,
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
        "pdf": None,
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
        "pdf": None,
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
        "pdf": None,
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
        "pdf": None,
    },
    {
        "titre": "First portfolio (HTML, Node.js, PostgreSQL)",
        "desc": "My first portfolio website, with a Node.js/Express server and a "
                "PostgreSQL database for the content.",
        "tags": ["HTML", "Node.js", "PostgreSQL"],
        "annee": 2024,
        "lien": "https://github.com/Tino971/portfolio",
        "image": "assets/project4.jpg",
        "pdf": None,
    },
    {
        "titre": "Bachelor's degree competencies database",
        "desc": "A Node.js/Express server with a PostgreSQL database for the "
                "competencies of my bachelor's degree.",
        "tags": ["Web", "SQL", "JavaScript"],
        "annee": 2025,
        "lien": None,
        "image": None,
        "pdf": None,
    },
]

PARCOURS = [
    ("2026 - 2028", "Master SIA (M1 in progress), Université Bourgogne Europe, Dijon"),
    ("2023 - 2026", "B.U.T. Data Science (VCOD track), IUT Besançon-Vesoul, Dole campus"),
    ("2023", "French Baccalauréat (Mathematics, Advanced Mathematics, Engineering Science), "
             "Lycée Gabriel Voisin, Tournus"),
]

EXPERIENCES = [
    ("2024 - 2026", "Data Analyst (apprenticeship)", "Tournus Équipement"),
    ("Jul - Aug 2024", "Packaging operator", "Bourgogne Repas, Cuisery"),
    ("Aug 2023", "Campsite assistant: reception, bar, activities", "Camping Saint-Martin, Sorèze"),
    ("Jul 2023", "Packaging operator", "Bourgogne Repas, Cuisery"),
]

LANGUES = {"French": "native", "English": "C1 (EF SET)", "Spanish": "B2"}

LOISIRS = ["Rugby", "Cooking", "Music", "Travel"]
