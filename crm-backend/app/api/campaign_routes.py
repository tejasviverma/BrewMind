from fastapi import APIRouter

from app.schemas.campaign_schema import (
    CampaignCreate,
    CampaignResponse,
    CampaignSendRequest,
    CampaignSendResponse
)

from app.services.campaign_service import (
    create_campaign,
    get_all_campaigns,
    send_campaign
)

router = APIRouter()


@router.post(
    "/campaigns",
    response_model=CampaignResponse
)
def create_new_campaign(
    campaign: CampaignCreate
):

    return create_campaign(campaign)

@router.get(
    "/campaigns",
    response_model=list[CampaignResponse]
)
def fetch_campaigns():

    return get_all_campaigns()

@router.post(
    "/campaigns/send",
    response_model=CampaignSendResponse
)
def send_campaign_route(
    request: CampaignSendRequest
):

    return send_campaign(
        request.campaign_id,
        request.segment
    )