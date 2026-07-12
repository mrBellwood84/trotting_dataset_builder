class Horse:

  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.SourceId = query_result[1]
    self.HorseSexId = query_result[2]
    self.HorseTypeId = query_result[3]
    self.Name = query_result[4]
    self.YearOfBirth = query_result[5]
    self.FatherSourceId = query_result[6]
    self.MotherSourceId = query_result[7]
    self.CreatedAt = query_result[8]
    self.UpdatedAt = query_result[9]

  def __str__(self):
    return f"""
            Id: {self.Id}
      SourceId: {self.SourceId}
    HorseSexId: {self.HorseSexId}
   HorseTypeId: {self.HorseTypeId}
          Name: {self.Name}
   YearOfBirth: {self.YearOfBirth}
FatherSourceId: {self.FatherSourceId}
MotherSourceId: {self.MotherSourceId}
     CreatedAt: {self.CreatedAt}
     UpdatedAt: {self.UpdatedAt}"""