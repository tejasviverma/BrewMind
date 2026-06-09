from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base

class CampaignRecipient(Base):
    __tablename__ = "campaign_recipients"

    id = Column(Integer, primary_key=True)

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id")
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    status = Column(String(50))