from lib.repository._BaseRepository import BaseRepository
from lib.models.Competition import Competition

class CompetitionRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=Competition, table_name="Competition")
