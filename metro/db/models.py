from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SObject(Base):
    __tablename__ = 'sobject'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    amount = Column(Integer, nullable=True)