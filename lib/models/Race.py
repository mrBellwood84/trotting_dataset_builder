class Race:

  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.CompetitionId = query_result[1]
    self.HorseTypeId = query_result[2]
    self.RaceStartTypeId = query_result[4]
    self.RaceNumber = query_result[3]
    self.StartTime = query_result[5]
    self.MainDistance = query_result[6]
    self.Monte = query_result[7]
    self.CreatedAt = query_result[8]
    self.UpdatedAt = query_result[9]

  def __str__(self):
    return f"""
             Id: {self.Id}
  CompetitionId: {self.CompetitionId}
    HorseTypeId: {self.HorseTypeId}
RaceStartTypeId: {self.RaceStartTypeId}
     RaceNumber: {self.RaceNumber}
      StartTime: {self.StartTime}
   MainDistance: {self.MainDistance}
          Monte: {self.Monte}
      CreatedAt: {self.CreatedAt}
      UpdatedAt: {self.UpdatedAt}"""
