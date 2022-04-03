from enum import unique
from data import Base
from sqlalchemy import String,Boolean,Integer,Column,Text

class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer)
    on_offer=Column(Boolean,default=False)