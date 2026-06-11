from pydantic import BaseModel


class HighValueCustomerResponse(BaseModel):

    customer_id: int
    customer_name: str
    total_spent: float


class HighValueAudienceSummaryResponse(BaseModel):

    audience_size: int
    average_spend: float

    top_city: str | None = None
    top_membership_tier: str | None = None