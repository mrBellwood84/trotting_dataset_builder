class DriverLicense:

    def __init__(self, query_result: list):
        self.Id = query_result[0]
        self.Code = query_result[1]
        self.Description = query_result[2]
        self.CreatedAt = query_result[3]
        self.UpdatedAt = query_result[4]

    def __str__(self):
        return f"""
         Id: {self.Id}
       Code: {self.Code}
Description: {self.Description}
  CreatedAt: {str(self.CreatedAt)}
  UpdatedAt: {str(self.UpdatedAt)} """
