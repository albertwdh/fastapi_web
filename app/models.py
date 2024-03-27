# -*- coding: UTF-8 -*- #
"""
@filename:models.py
@author:wdh
@time:2024-01-15
"""



from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from .database import Base
from sqlalchemy.orm import relationship
class Person(Base):
    __tablename__ = "Person"

    ID = Column(Integer(), primary_key=True)
    Name = Column(String(10))
    Age = Column(Integer())

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

