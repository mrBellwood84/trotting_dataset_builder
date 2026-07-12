class Driver:

  def __init__(self, query_result: list):
    self.Id = query_result[0]
    self.SourceId = query_result[1]
    self.DriverLicenseId = query_result[2]
    self.Name = query_result[3]
    self.YearOfBirth = query_result[4]
    self.Monte = query_result[5]
    self.CreatedAt = query_result[6]
    self.UpdatedAt = query_result[7]

  def __str__(self):
    return f"""
             Id: {self.Id}
       SourceId: {self.SourceId}
DriverLicenseId: {self.DriverLicenseId}
           Name: {self.Name}
    YearOfBirth: {self.YearOfBirth}
          Monte: {self.Monte}
      CreatedAt: {self.CreatedAt}
      UpdatedAt: {self.UpdatedAt}
"""