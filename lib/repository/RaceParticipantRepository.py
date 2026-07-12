from lib.repository._BaseRepository import BaseRepository
from lib.models.RaceParticipant import RaceParticipant

class RaceParticipantRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceParticipant, table_name="RaceParticipant")