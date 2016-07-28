from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from metro.api.client import SalesforceClient
from metro.db.models import Base

class DatabaseEngine(object):

    def __init__(self):
        config_engine = create_engine('postgresql://localhost/metro_config')
        Base.metadata.bind = config_engine
        ConfigSession = sessionmaker(bind=config_engine)
        self.config_session = ConfigSession()

        data_engine = create_engine('postgresql://localhost/metro_data')
        DataSession = sessionmaker(bind=data_engine)
        self.data_session = DataSession()

        self.source_client = SalesforceClient('', '')