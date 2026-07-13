from lib.repository.BaseRepository import BaseRepository
from lib.models.RaceParticipant import RaceParticipant

class RaceParticipantRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceParticipant, table_name="RaceParticipant")

  def get_participant_per_race(self, race_id):
    result = [x for x in self.data_list if x.RaceId == race_id]
    return result