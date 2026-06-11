from pydantic import BaseModel


class CustomerResponse(BaseModel):

    id: int
    name: str
    city: str
    membership_tier: str
    preferred_channel: str

    class Config:
        from_attributes = True

class CustomerSummaryResponse(BaseModel):

    customer_name: str
    city: str
    membership_tier: str
    preferred_channel: str
    total_orders: int
    total_spent: float
    favorite_product: str | None = None