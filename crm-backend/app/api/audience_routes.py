from fastapi import APIRouter

from app.services.audience_service import (
    get_high_value_customers,
    get_high_value_audience_summary
)

from app.schemas.audience_schema import (
    HighValueCustomerResponse,
    HighValueAudienceSummaryResponse
)

router = APIRouter()


@router.get(
    "/audience/high-value",
    response_model=list[HighValueCustomerResponse]
)
def fetch_high_value_customers():

    return get_high_value_customers()

@router.get(
    "/audience/high-value/summary",
    response_model=HighValueAudienceSummaryResponse
)
def fetch_high_value_audience_summary():

    return get_high_value_audience_summary()