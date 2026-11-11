import streamlit as st
from data import PROFIL
from outils import check, save

st.title("Contact")
st.write(f"You can send me a message with this form, or write to me at "
         f"[{PROFIL['email']}](mailto:{PROFIL['email']}).")

with st.form("contact"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Your message")
    sent = st.form_submit_button("Send")

if sent:
    erreurs = check(name, email, message)
    if erreurs:
        for e in erreurs:
            st.error(e)
    else:
        save(name, email, message)
        st.success("Thanks, your message has been sent.")
