from lib.repository._BaseRepository import BaseRepository
from lib.models.RaceResults import RaceResults

class RaceResultsRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceResults, table_name="RaceResults")