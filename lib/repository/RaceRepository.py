from lib.repository._BaseRepository import BaseRepository
from lib.models.Race import Race

class RaceRepository(BaseRepository): 
  def __init__(self):
    super().__init__(model_class=Race, table_name="Race")