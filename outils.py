import csv
import os
from datetime import datetime


def tous_les_tags(projets):
    tags = set()
    for p in projets:
        for tag in p["tags"]:
            tags.add(tag)
    return sorted(tags)


def filtrer_projets(projets, choisis):
    if not choisis:
        return projets
    resultat = []
    for p in projets:
        for tag in p["tags"]:
            if tag in choisis:
                resultat.append(p)
                break
    return resultat


def chercher_projets(projets, texte):
    texte = texte.strip().lower()
    if texte == "":
        return projets
    resultat = []
    for p in projets:
        if texte in p["titre"].lower() or texte in p["desc"].lower():
            resultat.append(p)
    return resultat


def verifier(nom, email, message):
    erreurs = []
    if nom.strip() == "":
        erreurs.append("Merci d'indiquer votre nom.")
    if "@" not in email or "." not in email.split("@")[-1]:
        erreurs.append("Merci d'indiquer un email valide.")
    if len(message.strip()) < 10:
        erreurs.append("Votre message est trop court (10 caractères minimum).")
    return erreurs


def enregistrer(nom, email, message):
    existe = os.path.exists("messages.csv")
    with open("messages.csv", "a", newline="", encoding="utf-8") as f:
        ecrivain = csv.writer(f)
        if not existe:
            ecrivain.writerow(["date", "nom", "email", "message"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        ecrivain.writerow([date, nom, email, message])


if __name__ == "__main__":
    from data import PROJETS

    print(tous_les_tags(PROJETS))
    for p in filtrer_projets(PROJETS, ["Interface graphique", "Power BI"]):
        print(p["titre"])
    print(len(filtrer_projets(PROJETS, [])), len(PROJETS))
    for p in chercher_projets(PROJETS, " SAP "):
        print(p["titre"])
    print(verifier("", "tino@gmail", "salut"))
    print(verifier("Tino", "tino@gmail.com", "Bonjour, ceci est un test."))
