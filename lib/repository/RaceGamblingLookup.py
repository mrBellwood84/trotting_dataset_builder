from lib.database.DbService import DbService
from lib.models.Race_RaceGamblingType import Race_RaceGamblingType

class RaceGamblingLookup:

  def __init__(self):
    self.data_list = []
    self.data_dict = {}

    self.query = "SELECT * FROM Race_RaceGamblingType"

  def load_data(self):
    db = DbService()
    raw_data = db.query(self.query)
    for item in raw_data:
      model = Race_RaceGamblingType(item)
      self.data_list.append(model)

  def count(self):
    return len(self.data_list)

  def get_gambling_types_for_race(self, race_id):
    result = [x for x in self.data_list if x.race_id == race_id]
    return result

