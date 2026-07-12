# TrottingData - Dataset Builder for Maskinlæring

Dette prosjektet har som formål å transformere ferdig innsamlet, relasjonell travdata fra en MySQL-database over til flate, strukturerte datasett skreddersydd for maskinlæring (ML). 

Målet med de endelige modellene er å predikere sannsynligheten (prosentandel) for henholdsvis 1. plass, 2. plass, 3. plass og topp 3-plassering, der hver modell opererer selvstendig.

*Merk: Alt av datainnhenting (skraping/ETL fra eksterne kilder) er utelatt fra dette repositoriet. Her jobbes det utelukkende med foredling av eksisterende data.*

---

## Arkitektur og Designmønstre

Prosjektet er sterkt inspirert av solide enterprise-mønstre (som Repository Pattern og Identity Map), men tilpasset Pythons dynamiske natur for å oppnå maksimal ytelse ($O(1)$ oppslagstid i minnet).

### 1. Modeller (`lib/models/`)
Hver tabell i databasen har en tilsvarende Python-klasse. Disse klassene har som oppgave å mappe en rå database-rad (tuple/list) til et sterkt typet objekt. Alle unike entiteter har en `Id`.

### 2. Repositorier (`lib/repository/`)
For å unngå tunge SQL `JOIN`-operasjoner som kveler databasen ved store datamengder, hentes tabellene rått inn i minnet (RAM) og struktureres i ordbøker (`dict`).
* **`_BaseRepository.py`:** En dynamisk baseklasse som automatisk håndterer lasting og mapping for standardtabeller basert på innsendt klasse og tabellnavn.
* **`RaceGamblingLookup.py`:** En spesialisert komponent (unntak fra basen) designet for å slå opp mange-til-mange-relasjoner mellom løp og spilletyper i minnet.

### 3. Database Service (`lib/database/`)
Enkel og rendyrket tilkoblingsklasse (`DbService.py`) som håndterer tilkobling mot MySQL og utfører spørringer. Den laster konfigurasjon autonomt fra en lokal `.env`-fil.

---

## Prosjektstruktur

```text
.
├── lib
│   ├── database
│   │   └── DbService.py          # Database-tilkobling og rå-spørringer
│   ├── models                    # Rene data-entiteter / Datamapping
│   │   ├── Competition.py
│   │   ├── Driver.py
│   │   ├── Horse.py
│   │   └── ... (øvrige domenemodeller)
│   └── repository                # In-memory data cashing og logikk
│       ├── _BaseRepository.py    # Generisk baseklasse for O(1) oppslag
│       ├── RaceGamblingLookup.py # Spesialoppslag for koblingstabell
│       └── ... (spesifikke repositorier)
├── data                          # Eksportmappe for genererte datasett (IGNORERT I GIT)
├── requirements.txt              # Prosjektets avhengigheter
└── README.md                     # Prosjekt-dokumentasjon

```

---

## Konfigurasjon (.env)

Prosjektet krever en `.env`-fil på roten av prosjektet med følgende format for å koble til databasen:

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=root
DB_NAME=trotting_data_no

```

---

## Arbeidsflyt for datasettbygging

1. **Eksperimentering:** Utvikling og testing av funksjoner (Feature Engineering), som historisk seiersprosent, galopp-risiko og kuskestatistikk, gjøres interaktivt i Jupyter Notebooks (`.ipynb`).
2. **Produksjon:** Når strukturen på datasettet er endelig verifisert, flyttes logikken over i rene Python-skripte (`.py`) for autonom generering av de endelige filene i `data/`-mappen.
