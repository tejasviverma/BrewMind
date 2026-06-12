from pydantic import BaseModel


class CampaignCreate(BaseModel):

    name: str
    goal: str
    message: str
    channel: str
    status: str


class CampaignResponse(BaseModel):

    id: int
    name: str
    goal: str
    message: str
    channel: str
    status: str

    class Config:
        from_attributes = True


class CampaignSendRequest(BaseModel):
    campaign_id: int
    segment: str


class CampaignSendResponse(BaseModel):
    campaign_id: int
    recipients: int
    status: str

class CampaignPerformanceResponse(BaseModel):

    campaign_id: int
    campaign_name: str

    total_recipients: int

    sent: int
    opened: int
    clicked: int

class CampaignInsightsResponse(BaseModel):

    open_rate: float

    click_rate: float

    best_city: str | None = None

    best_membership_tier: str | None = None