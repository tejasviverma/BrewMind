from fastapi import APIRouter

from app.schemas.campaign_schema import (
    CampaignCreate,
    CampaignInsightsResponse,
    CampaignResponse,
    CampaignSendRequest,
    CampaignSendResponse,
    CampaignPerformanceResponse,
    CampaignInsightsResponse
)

from app.services.campaign_service import (
    create_campaign,
    get_all_campaigns,
    send_campaign,
    get_campaign_performance,
    simulate_engagement,
    get_campaign_insights
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
def send_campaign_route(request: CampaignSendRequest):

    return send_campaign(
        request.campaign_id,
        request.segment
    )
@router.get(
    "/campaigns/{campaign_id}/performance",
    response_model=CampaignPerformanceResponse
)

def fetch_campaign_performance(campaign_id: int):

    return get_campaign_performance(
        campaign_id
    )

@router.post(
    "/campaigns/{campaign_id}/simulate-engagement"
)
def simulate_campaign_engagement(
    campaign_id: int
):

    return simulate_engagement(
        campaign_id
    )

@router.get(
    "/campaigns/{campaign_id}/insights",
    response_model=CampaignInsightsResponse
)
def fetch_campaign_insights(
    campaign_id: int
):

    return get_campaign_insights(
        campaign_id
    )