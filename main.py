import streamlit as st

# -------------------------------
# Woordenlijsten per niveau/blok
# -------------------------------

woordenlijsten = {
    "Niveau 1": {
        "Blok 1": {
            "Hallo": "Hola",
            "Tot ziens": "Adiós",
            "Dank je": "Gracias",
            "Alsjeblieft": "Por favor",
            "Ja": "Sí",
            "Nee": "No",
            "Huis": "Casa",
            "School": "Escuela",
            "Eten": "Comida",
            "Water": "Agua",
            "Vriend": "Amigo",
            "Familie": "Familia",
            "Werk": "Trabajo",
            "Boek": "Libro",
            "Hond": "Perro",
            "Kat": "Gato",
            "Auto": "Coche",
            "Stad": "Ciudad",
            "Land": "País",
            "Muziek": "Música"
        },
        "Blok 2": {
            "Ik werk": "Trabajo",
            "Ik werkte": "Trabajaba",
            "Ik ben aan het werk": "Estoy trabajando",
            "Ik heb gewerkt": "He trabajado",
            "Ik zal werken": "Trabajaré",
            "Ik zou werken": "Trabajaría",
            "Ik spreek": "Hablo",
            "Ik sprak": "Hablaba",
            "Ik ben aan het spreken": "Estoy hablando",
            "Ik heb gesproken": "He hablado",
            "Ik zal spreken": "Hablaré",
            "Ik zou spreken": "Hablaría"
        },
        "Blok 3": {
            "Ik ga naar school": "Voy a la escuela",
            "Ik eet een appel": "Como una manzana",
            "Ik woon in België": "Vivo en Bélgica",
            "Ik werk elke dag": "Trabajo cada día",
            "Ik lees een boek": "Leo un libro",
            "Ik luister naar muziek": "Escucho música"
        }
    }
}

# -------------------------------
# App-logica
# -------------------------------

st.title("🇪🇸 Spaans Oefenen 3.0")

niveau = st.selectbox("Kies je niveau:", list(woordenlijsten.keys()))
blok = st.selectbox("Kies je blok:", list(woordenlijsten[niveau].keys()))

woordenlijst = woordenlijsten[niveau][blok]
woorden = list(woordenlijst.items())

score = 0
fouten = []
voortgang = {}

for nederlands, spaans in woorden:
    antwoord = st.text_input(f"Wat is het Spaanse woord voor '{nederlands}'?", key=nederlands)
    if antwoord:
        if antwoord.strip().lower() == spaans.lower():
            st.success("✅ Juist!")
            score += 1
            voortgang[nederlands] = voortgang.get(nederlands, 0) + 1
        else:
            st.error(f"❌ Fout. Correct antwoord: {spaans}")
            fouten.append(nederlands)

# -------------------------------
# Resultaat en aanbeveling
# -------------------------------

if len(voortgang) == len(woorden):
    st.markdown("---")
    st.subheader("📊 Resultaat")
    st.write(f"Je scoorde {score} op {len(woorden)}")

    if score == len(woorden):
        st.success("🎉 Perfect! Je mag doorgaan naar het volgende blok.")
    elif score >= len(woorden) * 0.7:
        st.info("👍 Goed gedaan! Je mag doorgaan, maar herhalen kan geen kwaad.")
    else:
        st.warning(f"⚠️ Je scoorde minder dan 70%. We raden aan om '{blok}' van '{niveau}' opnieuw te doen.")

    # Automatisch doorschakelen
    niveaus = list(woordenlijsten.keys())
    blokken = list(woordenlijsten[niveau].keys())
    huidig_niveau_index = niveaus.index(niveau)
    huidig_blok_index = blokken.index(blok)

    if huidig_blok_index + 1 < len(blokken):
        volgende_blok = blokken[huidig_blok_index + 1]
        st.markdown(f"➡️ Volgende blok: **{volgende_blok}**")
    elif huidig_niveau_index + 1 < len(niveaus):
        volgende_niveau = niveaus[huidig_niveau_index + 1]
        st.markdown(f"⬆️ Volgende niveau: **{volgende_niveau}**, Blok 1")
    else:
        st.markdown("🏁 Je hebt alle blokken afgewerkt! Goed gedaan!")
