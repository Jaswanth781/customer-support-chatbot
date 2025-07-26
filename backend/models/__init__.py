from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    _tablename_ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    category = Column(String(255))
    price = Column(Float)
    stock = Column(Integer)