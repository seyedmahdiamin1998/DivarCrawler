# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy_utils import database_exists, create_database

from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DivarPipeline:

    def __init__(self):
        self.USER = 'postgres'
        self.PASSWORD = '1234'
        self.DATABASE_NAME = 'divar_db'
        self.SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{0}:{1}@localhost:5432/{2}".\
            format(self.USER, self.PASSWORD, self.DATABASE_NAME)
        self.create_myDatabase()
        self.create_connection()
        self.car = self.create_table_car()
            

    def create_myDatabase(self):
        '''
        Create a database to collect data there and if it exists don't do anything.
        '''
    
        is_database_exists = database_exists(self.SQLALCHEMY_DATABASE_URL)
        if not is_database_exists:
            engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
            create_database(engine.url)
            engine.dispose()
    

    def create_connection(self):
        '''
        Make connections here to use very where :)
        '''
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL, echo=False)
        self.Base = declarative_base()

        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def create_table_car(self):
        '''
        Create a table to collect cars data in there.
        '''
        class car(self.Base):
            __tablename__ = 'divar_car'
            id = Column(Integer, primary_key=True)
            name = Column(String(100))
            category = Column(String(100))
            model = Column(String(100))
            vehicleTransmission = Column(String(100))
            productionDate = Column(String(50))
            mileageFromOdometer = Column(Integer)
            knownVehicleDamages = Column(String(100))
            priceCurrency = Column(String(20))
            price = Column(String(100))
            color = Column(String(100))
            brand = Column(String(100))
            description = Column(String(1000))
            url = Column(String(1000))
                
        if not inspect(self.engine).has_table(self.DATABASE_NAME):
            self.Base.metadata.create_all(self.engine)

        return car


    def store_car(self, item):
        new_record = self.car(name = item['name'],
                              category = item['category'],
                              model = item['model'],
                              vehicleTransmission = item['vehicleTransmission'],
                              productionDate = item['productionDate'],
                              mileageFromOdometer = item['mileageFromOdometer'],
                              knownVehicleDamages = item['knownVehicleDamages'],
                              priceCurrency = item['priceCurrency'],
                              price = item['price'],
                              color = item['color'],
                              brand = item['brand'],
                              description = item['description'],
                              url = item['url'])

        self.session.add(new_record)
        self.session.commit()


    def process_item(self, item, spider):
        self.store_car(item)
        return item

# scrapy crawl mashhad