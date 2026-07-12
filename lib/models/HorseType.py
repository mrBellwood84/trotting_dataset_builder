import datetime

class HorseType:

    def __init__(self, query_result: list):
        self.Id = query_result[0]
        self.Type = query_result[1]
        self.CreatedAt = query_result[2]
        self.UpdatedAt = query_result[3]

    def __str__(self):
        return f"""
           Id: {self.Id}
         Type: {self.Type}
    CreatedAt: {self.CreatedAt}
    UpdatedAt: {self.UpdatedAt}"""
