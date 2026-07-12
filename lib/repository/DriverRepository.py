from lib.repository._BaseRepository import BaseRepository
from lib.models.Driver import Driver

class DriverRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=Driver, table_name="Driver", by_source_id=True)