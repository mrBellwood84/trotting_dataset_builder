from lib.database.DbService import DbService

class BaseRepository:

  def __init__(self, model_class, table_name, by_source_id: bool = False):

    self.model_class = model_class
    self.table_name = table_name
    self.by_source_id = by_source_id

    self.data_list: list = []
    self.data_dict: dict = {}
    self.query = f"SELECT * FROM {self.table_name}"

  def load_data(self):
    db = DbService()
    raw_data = db.query(self.query)
    for item in raw_data:
      model = self.model_class(item)
      self.data_list.append(model)
      if self.by_source_id: self.data_dict[model.SourceId] = model
      else: self.data_dict[model.Id] = model

  def count(self) -> int:
    return len(self.data_list)

  def get_by_id(self, item_id: str | None):
    if item_id is None: return None
    try:
      return self.data_dict[item_id]
    except KeyError:
      return None
