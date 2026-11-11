import csv
import os
from datetime import datetime


def all_tags(projets):
    tags = set()
    for p in projets:
        for tag in p["tags"]:
            tags.add(tag)
    return sorted(tags)


def filter_projects(projets, choisis):
    if not choisis:
        return projets
    resultat = []
    for p in projets:
        for tag in p["tags"]:
            if tag in choisis:
                resultat.append(p)
                break
    return resultat


def search_projects(projets, texte):
    texte = texte.strip().lower()
    if texte == "":
        return projets
    resultat = []
    for p in projets:
        if texte in p["titre"].lower() or texte in p["desc"].lower():
            resultat.append(p)
    return resultat


def check(name, email, message):
    erreurs = []
    if name.strip() == "":
        erreurs.append("Please enter your name.")
    if "@" not in email or "." not in email.split("@")[-1]:
        erreurs.append("Please enter a valid email.")
    if len(message.strip()) < 10:
        erreurs.append("Your message is too short (10 characters minimum).")
    return erreurs


def save(name, email, message):
    existe = os.path.exists("messages.csv")
    with open("messages.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["date", "name", "email", "message"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        writer.writerow([date, name, email, message])


if __name__ == "__main__":
    from data import PROJETS

    print(all_tags(PROJETS))
    for p in filter_projects(PROJETS, ["GUI", "Power BI"]):
        print(p["titre"])
    print(len(filter_projects(PROJETS, [])), len(PROJETS))
    for p in search_projects(PROJETS, " SAP "):
        print(p["titre"])
    print(check("", "tino@gmail", "salut"))
    print(check("Tino", "tino@gmail.com", "Bonjour, ceci est un test."))
