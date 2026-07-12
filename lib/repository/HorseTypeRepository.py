from lib.repository._BaseRepository import BaseRepository
from lib.models.HorseType import HorseType


class HorseTypeRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=HorseType, table_name="HorseType")