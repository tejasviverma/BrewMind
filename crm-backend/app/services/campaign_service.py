from app.db.database import SessionLocal
from app.models.campaign import Campaign
from app.models.campaign_recipient import CampaignRecipient
import random

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

def get_campaign_performance(campaign_id: int): 
    
    db = SessionLocal()

    campaign = (
        db.query(Campaign)
        .filter(
            Campaign.id == campaign_id
        )
        .first()
    )

    if not campaign:
        db.close()
        return None

    recipients = (
        db.query(CampaignRecipient)
        .filter(
            CampaignRecipient.campaign_id == campaign_id
        )
        .all()
    )

    total_recipients = len(recipients)

    sent_count = sum(1 for r in recipients if r.status == "Sent")
    opened_count = sum(1 for r in recipients if r.status == "Opened")
    clicked_count = sum(1 for r in recipients if r.status == "Clicked")

    db.close()

    return {
        "campaign_id": campaign.id,
        "campaign_name": campaign.name,
        "total_recipients": total_recipients,
        "sent": sent_count,
        "opened": opened_count,
        "clicked": clicked_count
    }

def simulate_engagement(campaign_id: int):

    db = SessionLocal()

    recipients = (
        db.query(CampaignRecipient)
        .filter(
            CampaignRecipient.campaign_id == campaign_id
        )
        .all()
    )

    for recipient in recipients:
        chance = random.random()

        if chance < 0.2:
            recipient.status = "Clicked"

        elif chance < 0.5:
            recipient.status = "Opened"

        else:
            recipient.status = "Sent"
        
    db.commit()
    db.close()

    return {
        "campaign_id": campaign_id,
        "updated_recipients": len(recipients),
        "message": "Engagement simulated successfully"
    }