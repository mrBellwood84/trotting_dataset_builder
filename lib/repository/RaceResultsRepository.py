from lib.repository.BaseRepository import BaseRepository
from lib.models.RaceResults import RaceResults

class RaceResultsRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceResults, table_name="RaceResults")

  def get_result_by_participant_id(self, participant_id):
    result = [x for x in self.data_list if x.RaceParticipantId == participant_id]
    if len(result) == 0: return None
    return result[0]
