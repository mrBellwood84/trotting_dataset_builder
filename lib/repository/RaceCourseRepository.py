from lib.repository.BaseRepository import BaseRepository
from lib.models.RaceCourse import RaceCourse

class RaceCourseRepository(BaseRepository):
  def __init__(self):
    super().__init__(model_class=RaceCourse, table_name="RaceCourse")