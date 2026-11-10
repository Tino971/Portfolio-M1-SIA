# Fonctions "pures" : pas de Streamlit ici, juste du Python.
# On peut donc les tester dans le terminal avec : python outils.py


def all_tags(projets):
    """Renvoie la liste triée des tags différents utilisés par les projets."""
    tags = set()  # un set garde chaque valeur une seule fois -> pas de doublons
    for p in projets:
        for tag in p["tags"]:
            tags.add(tag)
    return sorted(tags)  # sorted transforme le set en liste triée (ordre alphabétique)


def filter_projects(projets, choisis):
    """Renvoie les projets qui ont au moins un des tags choisis.
    Si aucun tag n'est choisi, renvoie tous les projets."""
    if not choisis:  # liste vide = pas de filtre
        return projets
    resultat = []
    for p in projets:
        for tag in p["tags"]:
            if tag in choisis:
                resultat.append(p)
                break  # projet déjà ajouté, inutile de regarder ses autres tags
    return resultat


# Ce bloc ne s'exécute que si on lance "python outils.py",
# pas quand une page fait "from outils import ...".
if __name__ == "__main__":
    from data import PROJETS

    print(all_tags(PROJETS))
    for p in filter_projects(PROJETS, ["GUI", "Power BI"]):
        print("-", p["titre"])
    print(len(filter_projects(PROJETS, [])), "projets sans filtre (attendu :", len(PROJETS), ")")
