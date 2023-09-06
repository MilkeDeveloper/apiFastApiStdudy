import uuid
from datetime import  date

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from sql_app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True, default=str(uuid.uuid4()))
    name = Column(String, index=True)
    email = Column(String, index=True)
    value = Column(Float)
    created_at = Column(Date)



