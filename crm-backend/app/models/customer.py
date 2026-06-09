from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True)

    phone = Column(String(20))

    city = Column(String(50))

    loyalty_points = Column(Integer, default=0)