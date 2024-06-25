# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Algorithm(Base):
    __tablename__ = "algorithms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(250))
    file_path = Column(String(250))
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="algorithms")
