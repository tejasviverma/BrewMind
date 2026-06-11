from app.db.database import SessionLocal
from app.models.campaign import Campaign
from app.models.campaign_recipient import CampaignRecipient

from app.services.audience_service import (
    get_high_value_customers
)


def create_campaign(campaign_data):

    db = SessionLocal()

    campaign = Campaign(
        name=campaign_data.name,
        goal=campaign_data.goal,
        message=campaign_data.message,
        channel=campaign_data.channel,
        status=campaign_data.status
    )

    db.add(campaign)

    db.commit()

    db.refresh(campaign)

    db.close()

    return campaign

def get_all_campaigns():

    db = SessionLocal()

    campaigns = (
        db.query(Campaign)
        .all()
    )

    db.close()

    return campaigns

def send_campaign(campaign_id: int, segment: str):

    db = SessionLocal()

    if segment == "high_value":

        customers = get_high_value_customers()

    else:

        db.close()

        return {
        "campaign_id": campaign_id,
        "recipients": 0,
        "status": "Invalid Segment"
        }
    
    for customer in customers:
        
        recipient = CampaignRecipient(
            campaign_id=campaign_id,
            customer_id=customer["customer_id"],
            status="Sent"
        )

        db.add(recipient)
    
    db.commit()

    campaign = (
    db.query(Campaign)
        .filter(
            Campaign.id == campaign_id
        )
        .first()
    )

    if campaign:
        campaign.status = "Sent"

    db.commit()

    recipient_count = len(customers)

    db.close()

    return {
        "campaign_id": campaign_id,
        "recipients": recipient_count,
        "status": "Sent"
    }