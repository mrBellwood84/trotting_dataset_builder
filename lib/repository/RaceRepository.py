from lib.repository._BaseRepository import BaseRepository
from lib.models.Race import Race

class RaceRepository(BaseRepository): 
  def __init__(self):
    super().__init__(model_class=Race, table_name="Race")

  def get_races_by_competition_id(self, competition_id):
    return [x for x in self.data_list if x.CompetitionId == competition_id]
