class RaceParticipant:
  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.RaceId = query_result[1]
    self.DriverSourceId = query_result[2]
    self.HorseSourceId = query_result[3]
    self.TrainerSourceId = query_result[4]
    self.CartTypeId = query_result[5]
    self.StartNumber = query_result[6]
    self.TrackNumber = query_result[7]
    self.TrackDistance = query_result[8]
    self.ForeShoe = query_result[9]
    self.HindShoe = query_result[10]
    self.CreatedAt = query_result[11]
    self.UpdatedAt = query_result[12]

  def __str__(self):
    return f"""
             Id: {self.Id}
         RaceId: {self.RaceId}
 DriverSourceId: {self.DriverSourceId}
  HorseSourceId: {self.HorseSourceId}
TrainerSourceId: {self.TrainerSourceId}
     CartTypeId: {self.CartTypeId}
    StartNumber: {self.StartNumber}
    TrackNumber: {self.TrackNumber}
  TrackDistance: {self.TrackDistance}
       ForeShoe: {self.ForeShoe}
       HindShoe: {self.HindShoe}
      CreatedAt: {self.CreatedAt}
      UpdatedAt: {self.UpdatedAt}"""

