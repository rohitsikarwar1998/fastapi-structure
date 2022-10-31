from sqlalchemy import Column, Integer, String
from config.database import Base

class Todos(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)