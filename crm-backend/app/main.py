from fastapi import FastAPI

from app.db.database import engine, Base

from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.campaign import Campaign
from app.models.campaign_recipient import CampaignRecipient

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "BrewMind API Running"
    }