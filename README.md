# TrottingData – EquiPredict Pipeline

Dette prosjektet er en høytytende, objektorientert feature engineering-pipeline utviklet for å foredle relasjonelle travdata fra en MySQL-database til flate, strukturerte datasett skreddersydd for maskinlæring (ML).

Målet med de endelige modellene er å predikere uavhengige sannsynligheter (prosentandeler) for:

* **1. plass**
* **2. plass**
* **3. plass**
* **Topp 3-plassering**

*Merk: Alt av rå datainnhenting (skraping/ETL fra eksterne kilder) er utelatt fra dette repositoriet. Her jobbes det utelukkende med foredling og transformasjon av eksisterende data.*

---

## 🏗️ Arkitektur og Designmønstre

Prosjektet er bygget etter strenge enterprise-prinsipper for å sikre maksimal ytelse, unngå tause feil ved bruk av løse ordbøker (`dicts`), og forhindre *data leakage* under feature-genereringen.

### 1. In-Memory Datalager & Repositorier (`lib/repository/`)

For å unngå tunge SQL `JOIN`-operasjoner som kveler databasen ved store datamengder, benytter prosjektet seg av **Identity Map**- og **Repository**-mønstre.

* Ved oppstart laster en felles **`DataRegistry`** samtlige tabeller rått inn i minnet (RAM) og indekserer dem.
* Dette gir en lynrask **$O(1)$ oppslagstid** på tvers av hele kjøringen. Baseklassen automatiserer mappingen fra databasetupler til sterkt typede objekter.

### 2. Domenemodeller (`lib/models/`)

Hver tabell i databasen har en tilsvarende ren Python-modell. Disse klassene representerer de virkelige entitetene i travsporten (hester, kusker, lisenser, baner) og sikrer typesikkerhet gjennom hele applikasjonen.

### 3. Builder-laget (`lib/builder/`)

Dette er hjertet i feature engineering-pipelinen. Transformasjonen er fullstendig objektorientert:

* **`DatasetBuilder`**: Hovedmotoren som orkestrerer byggeprosessen løp for løp, og håndterer avviste/ugyldige løp.
* **`RaceContext`**: Representerer hele feltet for ett spesifikt løp. Her beregnes **relative features** (f.eks. hvem som har høyest vinnerprosent på startstreken) før dataene flates ut.
* **`RaceDataRow`**: En sterkt typet dataklasse (DTO) som utgjør én rad i det endelige datasettet. Den garanterer riktig rekkefølge og kolonnenavn for eksport til Pandas.

---

## 📂 Prosjektstruktur

Applikasjonen er delt inn i logiske lag (separation of concerns):

```text
.
├── build_dataset.ipynb       # Interaktiv eksperimentering og pipeline-kjøring
├── lib/
│   ├── builder/              # Pipeline: Kapsler inn all Feature Engineering-logikk
│   ├── database/             # I/O: Håndterer den rå MySQL-tilkoblingen
│   ├── models/               # Entiteter: Sterkt typede domenemodeller
│   └── repository/           # RAM-Cache: In-memory O(1) oppslag for sportshistorikk
├── README.md
└── requirements.txt

```

---

## 🧼 Datasanering og Robusthet

Pipelinen håndterer aktivt ustrukturerte og støyende data fra sporten:

* **Km-tid-parsing (`KmTime`):** Rådata som `"24,5a"` (autostart) eller `"36,4ag"` (galopp) blir automatisk renset for bokstaver og konvertert til lineære desimaltall (`float`). Avansert logikk konverterer også eldre minutt-formater (f.eks `"1.14,5"`) til korrekte sekunder.
* **Ugyldige resultater / Avlysninger:** Hester som er strøket (`"STR"`), diskvalifisert (`"dg"`, `"g6 g"`) eller har brutt løpet (`"BR"`, `"br g"`) blir validert uten at programmet krasjer, slik at manglende verdier blir riktig representert som `None` / `NaN` for ML-modellen.

---

## ⚙️ Konfigurasjon (.env)

Prosjektet krever en `.env`-fil på rotmappen for å initialisere databasetilkoblingen automatisk:

```env
DB_HOST=host_address
DB_USER=user
DB_PASS=password
DB_NAME=db_name
```

