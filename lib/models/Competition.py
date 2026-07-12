class Competition:
  def __init__(self, query_results):
    self.Id = query_results[0]
    self.RaceCourseId = query_results[1]
    self.Date = query_results[2]
    self.FromDirectSource = query_results[3]
    self.CreatedAt = query_results[4]
    self.UpdatedAt = query_results[5]

  def __str__(self):
    return f"""
              Id: {self.Id}
    RaceCourseId: {self.RaceCourseId}
            Date: {self.Date}
FromDirectSource: {self.FromDirectSource}
       CreatedAt: {self.CreatedAt}
       UpdatedAt: {self.UpdatedAt}"""
