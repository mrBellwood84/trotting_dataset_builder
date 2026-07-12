import time
from typing import Optional
from tqdm.notebook import tqdm

# Importerer alle repositorier basert på dine PascalCase-filnavn
from lib.repository.CompetitionRepository import CompetitionRepository
from lib.repository.DriverLicenseRepository import DriverLicenseRepository
from lib.repository.DriverRepository import DriverRepository
from lib.repository.HorseRepository import HorseRepository
from lib.repository.HorseSexRepository import HorseSexRepository
from lib.repository.HorseTypeRepository import HorseTypeRepository
from lib.repository.RaceCartTypeRepository import RaceCartTypeRepository
from lib.repository.RaceCourseRepository import RaceCourseRepository
from lib.repository.RaceGamblingLookup import RaceGamblingLookup  # Spesialklassen din
from lib.repository.RaceGamblingTypeRepository import RaceGamblingTypeRepository
from lib.repository.RaceParticipantRepository import RaceParticipantRepository
from lib.repository.RaceRepository import RaceRepository
from lib.repository.RaceResultsRepository import RaceResultsRepository
from lib.repository.RaceStartTypeRepository import RaceStartTypeRepository


class DataRegistry:
    def __init__(self):
        # Eksplisitt deklarasjon for C#-følelse og full IntelliSense i Notebooks
        self.competitions: Optional[CompetitionRepository] = None
        self.driver_licenses: Optional[DriverLicenseRepository] = None
        self.drivers: Optional[DriverRepository] = None
        self.horses: Optional[HorseRepository] = None
        self.horse_sexes: Optional[HorseSexRepository] = None
        self.horse_types: Optional[HorseTypeRepository] = None
        self.race_cart_types: Optional[RaceCartTypeRepository] = None
        self.race_courses: Optional[RaceCourseRepository] = None
        self.race_gambling_lookup: Optional[RaceGamblingLookup] = None
        self.race_gambling_types: Optional[RaceGamblingTypeRepository] = None
        self.race_participants: Optional[RaceParticipantRepository] = None
        self.races: Optional[RaceRepository] = None
        self.race_results: Optional[RaceResultsRepository] = None
        self.race_start_types: Optional[RaceStartTypeRepository] = None

        # Mapping mellom feltnavn og selve klasse-typen for den autonome loopen
        self._repo_mapping = {
            "competitions": CompetitionRepository,
            "driver_licenses": DriverLicenseRepository,
            "drivers": DriverRepository,
            "horses": HorseRepository,
            "horse_sexes": HorseSexRepository,
            "horse_types": HorseTypeRepository,
            "race_cart_types": RaceCartTypeRepository,
            "race_courses": RaceCourseRepository,
            "race_gambling_lookup": RaceGamblingLookup,
            "race_gambling_types": RaceGamblingTypeRepository,
            "race_participants": RaceParticipantRepository,
            "races": RaceRepository,
            "race_results": RaceResultsRepository,
            "race_start_types": RaceStartTypeRepository,
        }

    def load_all(self):
        """Laster alle 14 datatabeller sekvensielt inn i RAM med en grafisk progress bar."""
        print("Starter opplasting av travdata til minnet...")
        start_time = time.time()

        # Oppretter Jupyter-progress bar
        pbar = tqdm(self._repo_mapping.items(), desc="Total fremdrift", unit="repo")

        for property_name, repo_class in pbar:
            # Oppdaterer teksten over baren dynamisk for hver tabell
            pbar.set_description(f"Laster {property_name}...")

            # Instansierer klassen (trigger _load_data() og SQL-kall internt)
            repo_instance = repo_class()

            # Setter instansen på riktig egenskap (f.eks. self.horses = HorseRepository())
            setattr(self, property_name, repo_instance)

        duration = time.time() - start_time
        print(
            f"✅ Suksess! Alle tabeller er cachet i minnet på {duration:.2f} sekunder."
        )