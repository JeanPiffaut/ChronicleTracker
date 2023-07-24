from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CharacterORM(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    year_of_birth = Column(String(100), nullable=True)
    month_of_birth = Column(String(100), nullable=True)
    day_of_birth = Column(String(100), nullable=True)
    status = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=True)
    life_status = Column(String(100), nullable=False)
