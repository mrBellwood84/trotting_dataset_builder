from lib.database.DbService import DbService

class BaseRepository:
  def __init__(self, model_class, table_name):

    self.model_class = model_class
    self.table_name = table_name

    self.data_list = []
    self.data_dict = {}
    self.query = f"SELECT * FROM {self.table_name}"

    self._load_data()

  def _load_data(self):
    db = DbService()
    raw_data = db.query(self.query)
    for item in raw_data:
      model = self.model_class(item)
      self.data_list.append(model)
      self.data_dict[model.Id] = model

  def count(self) -> int:
    return len(self.data_list)

  def get_by_id(self, item_id):
    return self.data_dict[item_id]