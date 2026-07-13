from time import time
from tqdm.auto import tqdm

from configurations import Config
from lib.builder.RaceContext import RaceContext
from lib.builder.RaceDataRow import RaceDataRow
from lib.models.Race import Race
from lib.models.RaceParticipant import RaceParticipant
from lib.repository.DataRegistry import DataRegistry

class DatasetBuilder:
  def __init__(self, registry: DataRegistry, config: Config):

    self.config: Config = config
    self.registry: DataRegistry = registry

    self.skipped_entries = 0
    self.processed_entries = 0

  def build(self) -> list[RaceContext]:

    result: list[RaceContext] = []

    print("Started building dataset...")
    races_to_solve = self.registry.races.data_list[:self.config.DATASET_BUILD_LIMIT]
    progress = tqdm(races_to_solve)

    start_time = time()

    for race in progress:
      context = self._resolve_race_context(race)
      participants = self.registry.race_participants.get_participant_per_race(race.Id)

      if len(participants) < self.config.MIN_PARTICIPANTS:
        self.skipped_entries += 1
        continue
      else: self.processed_entries += 1

      row_data = self._resolve_row_data(participants)
      context.race_rows = row_data

      result.append(context)

    duration = time() - start_time
    print(f"skipped entries: {self.skipped_entries}")
    print(f"processed entries: {self.processed_entries}")
    print(f"Done in {duration:.2f} seconds")
    return result

  def _resolve_race_context(self, race: Race) -> RaceContext:
    competition = self.registry.competitions.get_by_id(race.CompetitionId)
    race_course = self.registry.race_courses.get_by_id(competition.RaceCourseId)
    horse_type = self.registry.horse_types.get_by_id(race.HorseTypeId)
    start_type = self.registry.races_start_types.get_by_id(race.RaceStartTypeId)
    context = RaceContext(competition, race, race_course, horse_type, start_type)
    return context

  def _resolve_row_data(self, participants: list[RaceParticipant]):
    data: list[RaceDataRow] = []

    for participant in participants:
      race_result = self.registry.races_results.get_result_by_participant_id(participant.Id)
      cart = self.registry.race_carts.get_by_id(participant.CartTypeId)

      # skip row if driver or horse can not be resolved!
      driver = self.registry.drivers.get_by_id(participant.DriverSourceId)
      if driver is None: continue
      driver_license = self.registry.driver_licenses.get_by_id(driver.DriverLicenseId)

      horse = self.registry.horses.get_by_id(participant.HorseSourceId)
      if horse is None: continue
      horse_sex = self.registry.horse_sexes.get_by_id(horse.HorseSexId)
      horse_type = self.registry.horse_types.get_by_id(horse.HorseTypeId)

      trainer = self.registry.drivers.get_by_id(participant.TrainerSourceId)
      if trainer is None: trainer_license = None
      else: trainer_license = self.registry.driver_licenses.get_by_id(trainer.DriverLicenseId)

      item = RaceDataRow(participant, race_result)
      item.resolve_cart(cart)

      item.resolve_driver_data(driver, driver_license)
      item.resolve_trainer_data(trainer, trainer_license)
      item.resolve_horse_data(horse, horse_sex, horse_type)

      data.append(item)

    return data


    
