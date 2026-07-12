import re
from lib.models import Horse, Driver, DriverLicense, RaceParticipant, RaceResults, RaceCartType


def parse_km_time(km_time: str | None):
  if km_time is None: return 0;
  raw = str(km_time).strip()
  cleaned = re.sub(r'[^0-9.,]', '', raw)
  if cleaned == "": return 0
  cleaned = cleaned.replace(",", ".")
  number = float(cleaned)
  return number


class RaceDataRow:
  def __init__(self,
               participant: RaceParticipant,
               results: RaceResults):

    # participants meta data
    self.driver_source = participant.DriverSourceId
    self.driver_name = None
    self.driver_year_of_birth = None
    self.driver_license = None

    self.trainer_source = participant.TrainerSourceId
    self.trainer_name = None
    self._trainer_year_of_birth = None
    self.trainer_license = None

    self.horse_source = participant.HorseSourceId
    self.horse_name = None
    self.horse_sex = None
    self.horse_type = None
    self.horse_year_of_birth = None

    # startlist information
    self.start_number = participant.StartNumber
    self.track_number = participant.TrackNumber
    self.track_distance = participant.TrackDistance
    self.cart = None
    self.fore_shoe = participant.ForeShoe
    self.hind_shoe = participant.HindShoe

    # results information
    self.place = results.Place
    self.km_time = parse_km_time(results.KmTime)
    self.price = results.Price
    self.odds = results.Odds
    self.price = results.Price

    self.scratched = results.Scratched
    self.disqualified = results.Disqualified
    self.broken = results.Broken
    self.rremark = results.RRemark
    self.gremark = results.GRemark

  def resolve_driver_data(self, driver: Driver, license: DriverLicense):
    self.driver_name = driver.Name
    self.driver_year_of_birth = driver.YearOfBirth
    if license is not None: self.driver_license = license.Code

  def resolve_trainer_data(self, trainer: Driver | None, license: DriverLicense | None):
    if trainer is not None:
      self.trainer_name = trainer.Name
      self._trainer_year_of_birth = trainer.YearOfBirth
    if license is not None: self.trainer_license = license.Code

  def resolve_horse_data(self, horse: Horse, sex: str, horse_type: str):
    self.horse_name = horse.Name
    self.horse_sex = sex
    self.horse_type = horse_type
    self.horse_year_of_birth = horse.YearOfBirth

  def resolve_cart(self, cart_type: RaceCartType):
    if cart_type is not None:
      self.cart = cart_type.Type

  def __str__(self):
    return f""" -- Participant data --
    Driver Source Id: {self.driver_source}
         Driver Name: {self.driver_name}
Driver Year of Birth: {self.driver_year_of_birth}
      Driver License: {self.driver_license}

    Trainer Source Id: {self.trainer_source}
         Trainer Name: {self.trainer_name}
Trainer Year of Birth: {self._trainer_year_of_birth}
      Trainer License: {self.trainer_license}
      
    Horse Source Id: {self.horse_source}
         Horse Name: {self.horse_name}
          Horse Sex: {self.horse_sex}
         Horse Type: {self.horse_type}
Horse Year of Birth: {self.horse_year_of_birth}

 -- race meta data --
  Start Number: {self.start_number}
  Track Number: {self.track_number}
Track Distance: {self.track_distance}
          Cart: {self.cart}
     Fore Shoe: {self.fore_shoe}
     Hind Shoe: {self.hind_shoe}

 -- result data --
       Place: {self.place}
     Km Time: {self.km_time}
        Odds: {self.odds}
       Price: {self.price}
   Scratched: {self.scratched}
Disqualified: {self.disqualified}
      Broken: {self.broken}
     RRemark: {self.rremark}
     Gremark: {self.gremark}
"""


