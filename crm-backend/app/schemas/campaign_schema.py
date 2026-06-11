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