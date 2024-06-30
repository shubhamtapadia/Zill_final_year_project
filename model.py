from sqlalchemy import DateTime, create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from app import Base, engine


class Customer(Base):
    __tablename__='customer'
    id=Column(Integer, primary_key=True)
    name=Column(String(200), nullable=False)
    age=Column(Integer)

    def __str__(self):
        return self.name
    def serialize(self):
        return{
            "name":self.name,
            "age":self.age
        }
