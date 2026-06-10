from app.db.database import SessionLocal
from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order
from datetime import timedelta

from faker import Faker
import random

db = SessionLocal()
fake = Faker()

products = [
    ("Espresso", "Coffee", 120),
    ("Latte", "Coffee", 180),
    ("Cappuccino", "Coffee", 190),
    ("Mocha", "Coffee", 220),
    ("Cold Brew", "Coffee", 250),
    ("Americano", "Coffee", 150),
    ("Flat White", "Coffee", 210),
    ("Caramel Latte", "Coffee", 240),
    ("Hazelnut Latte", "Coffee", 260),
    ("Vanilla Cold Brew", "Coffee", 280),
]

if db.query(Product).count() == 0:

    for name, category, price in products:
        db.add(
            Product(
                name=name,
                category=category,
                price=price
            )
        )

    db.commit()

    print("Products inserted!")

membership_tiers = [
    "Silver",
    "Gold",
    "Platinum"
]

channels = [
    "WhatsApp",
    "Email",
    "SMS"
]

age_groups = [
    "18-25",
    "26-35",
    "36-50",
    "50+"
]

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune"
]

if db.query(Customer).count() == 0:

    for _ in range(500):

        tier = random.choices(
            membership_tiers,
            weights=[60, 30, 10]
        )[0]

        if tier == "Silver":
            loyalty = random.randint(0, 1000)

        elif tier == "Gold":
            loyalty = random.randint(1000, 5000)

        else:
            loyalty = random.randint(5000, 15000)

        customer = Customer(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number()[:20],
            city=random.choice(cities),
            loyalty_points=loyalty,
            preferred_channel=random.choice(channels),
            age_group=random.choice(age_groups),
            membership_tier=tier
        )

        db.add(customer)

    db.commit()

    print("500 customers inserted")

else:
    print("Customers already exist")

print("500 customers inserted!")

if db.query(Order).count() == 0:

    customers = db.query(Customer).all()
    products = db.query(Product).all()

    young_products = [4, 5, 8, 9, 10]
    older_products = [1, 2, 3, 6, 7]

    for _ in range(3000):

        customer = random.choice(customers)

        if customer.age_group in ["18-25", "26-35"]:
            product_id = random.choice(young_products)
        else:
            product_id = random.choice(older_products)

        product = next(
            p for p in products
            if p.id == product_id
        )

        if customer.membership_tier == "Platinum":
            quantity = random.randint(2, 5)

        elif customer.membership_tier == "Gold":
            quantity = random.randint(1, 4)

        else:
            quantity = random.randint(1, 2)

        order = Order(
            customer_id=customer.id,
            product_id=product.id,
            quantity=quantity,
            amount=product.price * quantity,
            order_date=fake.date_time_between(
                start_date="-365d",
                end_date="now"
            )
        )

        db.add(order)

    db.commit()

    print("3000 orders inserted")

else:
    print("Orders already exist")


db.close()