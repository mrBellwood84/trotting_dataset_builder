class RaceResults:

  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.RaceParticipantId = query_result[1]
    self.Place = query_result[2]
    self.KmTime = query_result[3]
    self.Odds = query_result[4]
    self.Price = query_result[5]
    self.Scratched = query_result[6]
    self.Disqualified = query_result[7]
    self.Broken = query_result[8]
    self.RRemark = query_result[9]
    self.GRemark = query_result[10]
    self.CreatedAt = query_result[11]
    self.UpdatedAt = query_result[12]

  def __str__(self):
    return f"""
               Id: {self.Id}
RaceParticipantId: {self.RaceParticipantId}
            Place: {self.Place}
           KmTime: {self.KmTime}
             Odds: {self.Odds}
            Price: {self.Price}
        Scratched: {self.Scratched}
     Disqualified: {self.Disqualified}
           Broken: {self.Broken}
          RRemark: {self.RRemark}
          GRemark: {self.GRemark}
        CreatedAt: {self.CreatedAt}
        UpdatedAt: {self.UpdatedAt} """