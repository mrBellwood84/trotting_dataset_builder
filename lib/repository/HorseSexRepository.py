from lib.repository.BaseRepository import BaseRepository
from lib.models.HorseSex import HorseSex

class HorseSexRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=HorseSex, table_name="HorseSex")
