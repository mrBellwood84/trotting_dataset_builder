from lib.repository._BaseRepository import BaseRepository
from lib.models.DriverLicense import DriverLicense

class DriverLicenseRepository(BaseRepository):
    def __init__(self):
        super().__init__(model_class=DriverLicense, table_name="DriverLicense")