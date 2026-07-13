from lib.repository.BaseRepository import BaseRepository
from lib.models.RaceStartType import RaceStartType

class RaceStartTypeRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceStartType, table_name="RaceStartType")