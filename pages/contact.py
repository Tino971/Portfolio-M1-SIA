import streamlit as st
from data import PROFIL
from outils import verifier, enregistrer

st.title("Contact")
st.write(f"Vous pouvez m'envoyer un message avec ce formulaire, ou m'écrire à "
         f"[{PROFIL['email']}](mailto:{PROFIL['email']}).")

with st.form("contact"):
    nom = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    message = st.text_area("Votre message")
    envoye = st.form_submit_button("Envoyer")

if envoye:
    erreurs = verifier(nom, email, message)
    if erreurs:
        for e in erreurs:
            st.error(e)
    else:
        enregistrer(nom, email, message)
        st.success("Merci, votre message a bien été envoyé.")
