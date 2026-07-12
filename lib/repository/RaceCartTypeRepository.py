from lib.repository._BaseRepository import BaseRepository
from lib.models.RaceCartType import RaceCartType

class RaceCartTypeRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceCartType, table_name="RaceCartType")