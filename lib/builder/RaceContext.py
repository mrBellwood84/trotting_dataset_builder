from lib.builder import RaceDataRow
from lib.models import Competition, Race, RaceCourse, HorseType, RaceStartType

class RaceContext:
  def __init__(self,
               competition: Competition,
               race: Race,
               race_course: RaceCourse,
               horse_type: HorseType | None,
               start_type: RaceStartType):

    self.id = race.Id
    self.date = competition.Date
    self.race_course = race_course.Name
    self.race_number = race.RaceNumber
    self.distance = race.MainDistance
    self.start_type = start_type.Type
    self.monte = race.Monte

    if horse_type is not None: self.horse_type = horse_type.Type
    else: self.horse_type = None

    self.race_rows: list[RaceDataRow] = []

  def __str__(self):
    return f"""
          Id: {self.id}
        Date: {self.date}
 Race Course: {self.race_course}
 Race Number: {self.race_number}
    Distance: {self.distance}
  Start Type: {self.start_type}
  Horse Type: {self.horse_type}
       Monte: {self.monte}
Participants: {len(self.race_rows)}"""

