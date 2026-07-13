import time
from tqdm.auto import tqdm

from lib.repository import BaseRepository
from lib.repository.CompetitionRepository import CompetitionRepository
from lib.repository.DriverLicenseRepository import DriverLicenseRepository
from lib.repository.DriverRepository import DriverRepository
from lib.repository.HorseRepository import HorseRepository
from lib.repository.HorseSexRepository import HorseSexRepository
from lib.repository.HorseTypeRepository import HorseTypeRepository
from lib.repository.RaceCartTypeRepository import RaceCartTypeRepository
from lib.repository.RaceCourseRepository import RaceCourseRepository
from lib.repository.RaceGamblingLookup import RaceGamblingLookup
from lib.repository.RaceGamblingTypeRepository import RaceGamblingTypeRepository
from lib.repository.RaceParticipantRepository import RaceParticipantRepository
from lib.repository.RaceRepository import RaceRepository
from lib.repository.RaceResultsRepository import RaceResultsRepository
from lib.repository.RaceStartTypeRepository import RaceStartTypeRepository

class DataRegistry:

  def __init__(self):
    self.competitions = CompetitionRepository()
    self.drivers = DriverRepository()
    self.driver_licenses = DriverLicenseRepository()
    self.horses = HorseRepository()
    self.horse_sexes = HorseSexRepository()
    self.horse_types = HorseTypeRepository()
    self.race_carts = RaceCartTypeRepository()
    self.race_courses = RaceCourseRepository()
    self.race_gambling_lookup = RaceGamblingLookup()
    self.race_gambling_types = RaceGamblingTypeRepository()
    self.races = RaceRepository()
    self.race_participants = RaceParticipantRepository()
    self.races_results = RaceResultsRepository()
    self.races_start_types = RaceStartTypeRepository()

    self.__repo_map: dict[str, type[BaseRepository]] = {
      "competitions": self.competitions,
      "drivers": self.drivers,
      "driver_licenses": self.driver_licenses,
      "horses": self.horses,
      "horse_sexes": self.horse_sexes,
      "horse_types": self.horse_types,
      "race_carts": self.race_carts,
      "race_courses": self.race_courses,
      "race_gambling_lookup": self.race_gambling_lookup,
      "race_gambling_types": self.race_gambling_types,
      "races": self.races,
      "race_participants": self.race_participants,
      "races_results": self.races_results,
      "races_start_types": self.races_start_types,
    }

  def load_all(self):
    print("Loading repo data...")
    start_time = time.time()

    progress = tqdm(self.__repo_map.items())

    for name, repo in progress:
      repo.load_data()

    duration = time.time() - start_time
    print(f"Done in {duration:.2f} seconds")

