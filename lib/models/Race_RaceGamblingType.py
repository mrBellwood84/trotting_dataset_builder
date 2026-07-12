class Race_RaceGamblingType:

  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.RaceId = query_result[1]
    self.RaceGamblingTypeId = query_result[2]

  def __str__(self):
    return f"""
                Id: {self.Id}
            RaceId: {self.RaceId}
RaceGamblingTypeId: {self.RaceGamblingTypeId}
"""