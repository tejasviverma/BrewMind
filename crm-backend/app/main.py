from fastapi import FastAPI
from app.api.customer_routes import router as customer_router
from app.db.database import engine, Base

from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.campaign import Campaign
from app.models.campaign_recipient import CampaignRecipient
from app.api.audience_routes import (
    router as audience_router
)
from app.api.campaign_routes import router as campaign_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(customer_router)
app.include_router(audience_router)
app.include_router(campaign_router)

@app.get("/")
def root():
    return {
        "message": "BrewMind API Running"
    }