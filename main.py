import streamlit as st
import random

st.set_page_config(page_title="Spaans oefenen", page_icon="🇪🇸")

woordenlijst = {
    "perro": "hond",
    "gato": "kat",
    "casa": "huis",
    "libro": "boek",
    "escuela": "school",
    "comida": "eten",
    "agua": "water",
    "amigo": "vriend",
    "familia": "familie",
    "trabajo": "werk"
}

if "score" not in st.session_state:
    st.session_state.score = {woord: 0 for woord in woordenlijst}
if "huidig_woord" not in st.session_state:
    st.session_state.huidig_woord = random.choice(list(woordenlijst.keys()))

st.title("🇪🇸 Spaans oefenen")
st.write("Vertaal het Spaanse woord naar het Nederlands.")

st.write(f"**Woord:** {st.session_state.huidig_woord}")
antwoord = st.text_input("Jouw antwoord:")

if st.button("Controleer"):
    juist = woordenlijst[st.session_state.huidig_woord]
    if antwoord.strip().lower() == juist:
        st.success("✅ Juist!")
        st.session_state.score[st.session_state.huidig_woord] += 1
        if st.session_state.score[st.session_state.huidig_woord] == 2:
            st.write(f"🎉 '{st.session_state.huidig_woord}' is nu geleerd!")
            del st.session_state.score[st.session_state.huidig_woord]
    else:
        st.error(f"❌ Fout. Het juiste antwoord is: {juist}")
    if st.session_state.score:
        st.session_state.huidig_woord = random.choice(list(st.session_state.score.keys()))
    else:
        st.balloons()
        st.write("🎓 Je hebt alle woorden geleerd!")

if st.button("Reset"):
    st.session_state.score = {woord: 0 for woord in woordenlijst}
    st.session_state.huidig_woord = random.choice(list(woordenlijst.keys()))
    st.experimental_rerun()
