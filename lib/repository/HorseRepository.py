from lib.repository.BaseRepository import BaseRepository
from lib.models.Horse import Horse


class HorseRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=Horse, table_name="Horse",by_source_id=True)