import datetime

class RaceCourse:

    def __init__(self, query_result: list):
        self.Id = query_result[0]
        self.Name = query_result[1]
        self.CreatedAt = query_result[2]
        self.UpdatedAt = query_result[3]

    def __str__(self):
        return f"""
       Id: {self.Id}
     Name: {self.Name}
CreatedAt: {self.CreatedAt}
UpdatedAt: {self.UpdatedAt}
"""