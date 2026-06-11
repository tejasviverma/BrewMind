from fastapi import APIRouter

from app.services.customer_service import (
    get_all_customers
)

from app.schemas.customer_schema import (
    CustomerResponse
)

from app.services.customer_service import (
    get_all_customers,
    get_customer_summary
)

from app.schemas.customer_schema import (
    CustomerResponse,
    CustomerSummaryResponse
)

from app.services.customer_service import get_customers_by_city
from app.services.customer_service import get_customers_by_tier
from app.services.customer_service import get_customers_by_channel

router = APIRouter()


@router.get(
    "/customers",
    response_model=list[CustomerResponse]
)
def fetch_customers():

    return get_all_customers()

@router.get(
    "/customers/{customer_id}/summary",
    response_model=CustomerSummaryResponse
)
def fetch_customer_summary(customer_id: int):

    return get_customer_summary(customer_id)

@router.get("/audience/by-city/{city}")
def fetch_customers_by_city(city: str):

    return get_customers_by_city(city)

@router.get("/audience/by-tier/{tier}")
def fetch_customers_by_tier(tier: str):

    return get_customers_by_tier(tier)

@router.get("/audience/by-channel/{channel}")
def fetch_customers_by_channel(channel: str):

    return get_customers_by_channel(channel)