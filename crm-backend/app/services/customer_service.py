from sqlalchemy import func

from app.db.database import SessionLocal

from app.models.customer import Customer
from app.models.order import Order
from app.models.product import Product

def get_all_customers():

    db = SessionLocal()

    customers = db.query(Customer).all()

    db.close()

    return customers

def get_customer_summary(customer_id: int):

    db = SessionLocal()

    customer = (
        db.query(Customer)
        .filter(
            Customer.id == customer_id
        )
        .first()
    )

    if not customer:
        db.close()
        return None

    total_orders = (
        db.query(Order)
        .filter(
            Order.customer_id == customer_id
        )
        .count()
    )

    total_spent = (
        db.query(
            func.sum(Order.amount)
        )
        .filter(
            Order.customer_id == customer_id
        )
        .scalar()
    ) or 0

    favorite_product_row = (
        db.query(
            Order.product_id,
            func.count(Order.product_id).label("purchase_count")
        )
        .filter(
            Order.customer_id == customer_id
        )
        .group_by(Order.product_id)
        .order_by(
            func.count(Order.product_id).desc()
        )
        .first()
    )

    favorite_product = None

    if favorite_product_row:

        product = (
            db.query(Product)
            .filter(
                Product.id == favorite_product_row[0]
            )
            .first()
        )

        if product:
            favorite_product = product.name

    db.close()

    return {
        "customer_name": customer.name,
        "city": customer.city,
        "membership_tier": customer.membership_tier,
        "preferred_channel": customer.preferred_channel,
        "total_orders": total_orders,
        "total_spent": total_spent,
        "favorite_product": favorite_product
    }

def get_customers_by_city(city: str):

    db = SessionLocal()

    customers = (
        db.query(Customer)
        .filter(
            Customer.city == city
        )
        .all()
    )

    db.close()

    return customers

def get_customers_by_tier(tier: str):

    db = SessionLocal()

    customers = (
        db.query(Customer)
        .filter(
            Customer.membership_tier == tier
        )
        .all()
    )

    db.close()

    return customers

def get_customers_by_channel(channel: str):

    db = SessionLocal()

    customers = (
        db.query(Customer)
        .filter(
            Customer.preferred_channel == channel
        )
        .all()
    )

    db.close()

    return customers