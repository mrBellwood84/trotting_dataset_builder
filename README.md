# 🐍 Trotting CSV Builder

Dette er en minimalistisk og uavhengig Python-klient utviklet for å hente ferdig foredlede og verifiserte løpsdata fra et eksternt C# API via JSON, for så å flate dem ut og skrive dem direkte til CSV-filer for maskinlæring.

Prosjektet gjør ingen tung datavalidering, filtrering eller databasesøk under selve kjøringen. All kjerne-logikk er delegert til C#-backend.

---

## 🏗️ Arkitektur & Dataflyt

Selve datalinje-byggeren er 100 % frikoblet fra databasen og opererer utelukkende over HTTP:

```text
[ C# API (Backend) ] ───( JSON via HTTP )───> [ Trotting CSV Builder ] ───> [ Eksport: CSV ]

```

* **Ren JSON-strøm:** Klienten ber om data, mottar strukturerte JSON-rekker, og dytter dem rett i en flat CSV-fil.
* **Håndtering av tomme løp:** Hvis et løp eller en konkurranse ikke inneholder noen godkjente eller verifiserte data, returnerer C# API-et en tom liste (`[]`). Python-klienten hopper da bare elegant videre til neste iterasjon uten ekstra støy.

---

## ⚙️ Kjørestrategi (Pipeline-logikk)

Siden databasen inneholder over 400 000 individuelle løp, er pipelinen strukturert rundt **konkurranser** (~77 000 stykker) for å minimere antall API-kall og sikre en mer effektiv kjøring:

1. **Hent Konkurranser:** Skriptet gjør et innledende kall for å hente en liste over alle tilgjengelige `CompetitionID`-er.
2. **Hent Løp per Konkurranse:** For hver unike konkurranse hentes listen med tilhørende `RaceID`-er.
3. **Hent og Skriv Datalinjer:** Skriptet forespør de ferdige datarekkene for hvert enkelt `RaceID`, transformerer JSON-responsen til CSV-format, og appender (legger til) linjene fortløpende til filen.

---

## 🛠️ Standalone Verktøy (Notebooks)

Prosjektet inkluderer også frittstående Jupyter Notebooks. Disse er **helt dekuplet** fra selve CSV-byggeren og kjøres kun manuelt ved behov:

* Ad-hoc database-cleanup for å tette hull i dataene.
* Identifisering og tildeling av anonyme/generiske profiler ("ghosts") til ukjente hester eller kusker direkte i MySQL.

---

## ⚙️ Konfigurasjon (`.env`)

Opprett en `.env`-fil på rotmappen med endepunktet til API-et ditt (og eventuelle database-detaljer dedikert kun til cleanup-notebooks):

```env
# API-tilkobling for CSV Builder
API_BASE_URL=http://localhost:5000/api

# Database (Kun brukt lokalt av cleanup-notebooks)
DB_HOST=localhost
DB_USER=ditt_brukernavn
DB_PASS=ditt_passord
DB_NAME=trotting_db

```