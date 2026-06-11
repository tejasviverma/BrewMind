from collections import Counter

from sqlalchemy import func

from app.db.database import SessionLocal

from app.models.customer import Customer
from app.models.order import Order


def get_high_value_customers():

    db = SessionLocal()

    results = (
        db.query(
            Customer.id,
            Customer.name,
            func.sum(Order.amount).label("total_spent")
        )
        .join(
            Order,
            Customer.id == Order.customer_id
        )
        .group_by(
            Customer.id,
            Customer.name
        )
        .having(
            func.sum(Order.amount) > 5000
        )
        .all()
    )

    db.close()

    return [
        {
            "customer_id": row.id,
            "customer_name": row.name,
            "total_spent": row.total_spent
        }
        for row in results
    ]


def get_high_value_audience_summary():

    db = SessionLocal()

    high_value_customers = (
        db.query(
            Customer.id,
            Customer.city,
            Customer.membership_tier,
            func.sum(Order.amount).label("total_spent")
        )
        .join(
            Order,
            Customer.id == Order.customer_id
        )
        .group_by(
            Customer.id,
            Customer.city,
            Customer.membership_tier
        )
        .having(
            func.sum(Order.amount) > 5000
        )
        .all()
    )

    audience_size = len(high_value_customers)

    average_spend = 0

    if audience_size > 0:

        average_spend = (
            sum(
                customer.total_spent
                for customer in high_value_customers
            )
            / audience_size
        )

    city_counts = Counter(
        customer.city
        for customer in high_value_customers
    )

    top_city = None

    if city_counts:
        top_city = city_counts.most_common(1)[0][0]

    tier_counts = Counter(
        customer.membership_tier
        for customer in high_value_customers
    )

    top_membership_tier = None

    if tier_counts:
        top_membership_tier = (
            tier_counts.most_common(1)[0][0]
        )

    db.close()

    return {
        "audience_size": audience_size,
        "average_spend": round(average_spend, 2),
        "top_city": top_city,
        "top_membership_tier": top_membership_tier
    }