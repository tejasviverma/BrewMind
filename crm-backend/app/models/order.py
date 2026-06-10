from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer)

    amount = Column(Float)

    order_date = Column(
        DateTime,
        default=datetime.utcnow
    )