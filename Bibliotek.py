import json  # Vi bruker JSON for å lagre og hente data fra en fil

FILNAVN = "bibliotek.json"  # Filen der vi lagrer biblioteket

# Funksjon for å lagre biblioteket til fil
def lagre_data():
    with open(FILNAVN, "w", encoding="utf-8") as f:
        json.dump(bibliotek, f, ensure_ascii=False, indent=4)

# Funksjon for å laste inn biblioteket fra fil
def laste_data():
    try:
        with open(FILNAVN, "r", encoding="utf-8") as f:
            return json.load(f)  # Leser inn data hvis filen finnes
    except FileNotFoundError:
        return []  # Hvis filen ikke finnes, starter vi med et tomt bibliotek

# Laster inn eksisterende bøker eller starter tomt
bibliotek = laste_data()

# Funksjon for å legge til en ny bok
def legg_til_bok():
    tittel = input("Hva heter boka? ")
    forfatter = input("Hvem har skrevet den? ")
    bok = {"tittel": tittel, "forfatter": forfatter, "status": "Tilgjengelig"}
    bibliotek.append(bok)  # Legger boka inn i lista
    lagre_data()  # Oppdaterer filen
    print(f"📖 '{tittel}' lagt til i biblioteket!")

# Funksjon for å vise alle bøker
def vis_bøker():
    if not bibliotek:  # Hvis listen er tom
        print("😅 Biblioteket er tomt!")
        return
    print("\nHer er alle bøkene våre:")
    for i, bok in enumerate(bibliotek, 1):  # Viser alle bøker med nummerering
        print(f"{i}. {bok['tittel']} av {bok['forfatter']} → {bok['status']}")

# Funksjon for å låne en bok
def lån_bok():
    søk = input("Skriv tittel eller forfatter for å låne bok: ").lower()
    for bok in bibliotek:
        # Sjekker om søket finnes i tittel eller forfatter
        if søk in bok['tittel'].lower() or søk in bok['forfatter'].lower():
            if bok['status'] == "Tilgjengelig":  # Hvis boka er ledig
                bok['status'] = "Utlånt"
                lagre_data()
                print(f"✅ Du har lånt '{bok['tittel']}'!")
                return
            else:
                print(f"⚠️ '{bok['tittel']}' er allerede utlånt.")
                return
    print("🤔 Fant ingen bok som matcher.")

# Funksjon for å levere en bok tilbake
def lever_bok():
    søk = input("Skriv tittel eller forfatter for å levere inn bok: ").lower()
    for bok in bibliotek:
        if søk in bok['tittel'].lower() or søk in bok['forfatter'].lower():
            if bok['status'] == "Utlånt":  # Hvis boka er lånt ut
                bok['status'] = "Tilgjengelig"
                lagre_data()
                print(f"🙌 Takk for at du leverte '{bok['tittel']}'!")
                return
            else:
                print(f"🤔 '{bok['tittel']}' var ikke utlånt.")
                return
    print("😅 Fant ingen bok som matcher.")

# --- Hovedmeny ---
while True:
    print("\n--- Velkommen til biblioteket! ---")
    print("1️⃣  Legg til bok")
    print("2️⃣  Se alle bøker")
    print("3️⃣  Lån en bok")
    print("4️⃣  Lever inn en bok")
    print("5️⃣  Avslutt")

    valg = input("Hva vil du gjøre? ")

    if valg == "1":
        legg_til_bok()  # Kaller funksjon for å legge til bok
    elif valg == "2":
        vis_bøker()  # Kaller funksjon for å vise alle bøker
    elif valg == "3":
        lån_bok()  # Kaller funksjon for å låne bok
    elif valg == "4":
        lever_bok()  # Kaller funksjon for å levere bok
    elif valg == "5":
        print("👋 Ha det! Biblioteket stenger nå.")
        break  # Avslutter løkken
    else:
        print("⚠️ Ugyldig valg, prøv igjen!")
