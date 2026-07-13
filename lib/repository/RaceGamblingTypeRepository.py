from lib.repository.BaseRepository import BaseRepository
from lib.models.RaceGamblingType import RaceGamblingType

class RaceGamblingTypeRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceGamblingType, table_name="RaceGamblingType")