 BrewMind CRM Backend

A scalable CRM backend built with FastAPI, MySQL, and SQLAlchemy to help businesses manage customers, track purchases, segment audiences, and analyze marketing campaign performance.

Overview

BrewMind simulates a real-world Customer Relationship Management (CRM) platform that enables businesses to:

 Manage customer and order data
 Identify high-value customers
 Create and send marketing campaigns
 Track campaign engagement
 Generate actionable business insights

The project focuses on backend architecture, REST API development, database design, and analytics generation.

Features

Customer Management

 Store and manage customer information
 View customer purchase history
 Generate customer spending summaries

Order Management

 Track purchases across products
 Calculate customer spending patterns

Customer Segmentation

 Identify high-value customers
 Analyze spending behavior
 Support targeted marketing campaigns

Campaign Management

 Create marketing campaigns
 Send campaigns to customer segments
 Track recipient engagement

Analytics & Insights

 Open Rate Calculation
 Click Rate Calculation
 Audience Size Metrics
 Best Performing City Analysis
 Best Membership Tier Analysis

API Documentation

  Interactive Swagger UI
  OpenAPI Specifications


System Architecture

```text
                        Frontend Dashboard
                                │
                                ▼
                        FastAPI REST APIs
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼

   Customer Service     Campaign Service     Analytics Service

                                │
                                ▼

                         SQLAlchemy ORM
                                │
                                ▼

                           MySQL Database
```


Tech Stack

Backend

 Python
 FastAPI
 Uvicorn

Database

 MySQL
 SQLAlchemy ORM
 PyMySQL

Data Generation

 Faker

 Deployment

  Render
  Railway

Development Tools

  Git
  GitHub
  Swagger/OpenAPI

Project Structure

```bash
brewmind/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── campaign.py
│   │   └── campaign_recipient.py
│   │
│   ├── services/
│   │   ├── customer_service.py
│   │   ├── campaign_service.py
│   │   └── analytics_service.py
│   │
│   ├── routes/
│   │   ├── customers.py
│   │   ├── campaigns.py
│   │   └── analytics.py
│   │
│   └── schemas/
│
├── seed_data.py
├── requirements.txt
└── README.md
```

Database Schema

Customer

| Column          | Type    |
| --------------- | ------- |
| id              | Integer |
| name            | String  |
| email           | String  |
| age             | Integer |
| city            | String  |
| membership_tier | String  |

Product

| Column | Type    |
| ------ | ------- |
| id     | Integer |
| name   | String  |
| price  | Float   |

Order

| Column      | Type        |
| ----------- | ----------- |
| id          | Integer     |
| customer_id | Foreign Key |
| product_id  | Foreign Key |
| quantity    | Integer     |
| amount      | Float       |
| order_date  | Date        |

Campaign

| Column     | Type     |
| ---------- | -------- |
| id         | Integer  |
| name       | String   |
| message    | Text     |
| created_at | DateTime |

CampaignRecipient

| Column      | Type                    |
| ----------- | ----------------------- |
| id          | Integer                 |
| campaign_id | Foreign Key             |
| customer_id | Foreign Key             |
| status      | Sent / Opened / Clicked |



Entity Relationships

```text
Customer
   │
   ├──< Orders

Campaign
   │
   └──< CampaignRecipients >── Customer
```

Analytics Implemented

Customer Analytics

  Total Orders
  Total Spend
  Average Spend
  High-Value Customer Detection

Campaign Analytics

  Total Recipients
  Sent Count
  Opened Count
  Clicked Count
  Open Rate
  Click Rate
  Best Performing City
  Best Membership Tier


API Endpoints

Customers

Get All Customers

```http
GET /customers
```

Customer Summary

```http
GET /customers/{customer_id}/summary
```

High Value Customers

```http
GET /customers/high-value
```

Campaigns

Create Campaign

```http
POST /campaigns
```

Get All Campaigns

```http
GET /campaigns
```

Send Campaign

```http
POST /campaigns/{campaign_id}/send
```

Analytics

Campaign Performance

```http
GET /campaigns/{campaign_id}/performance
```

Campaign Insights

```http
GET /campaigns/{campaign_id}/insights
```

Seed Data

The project includes a custom Faker-based data generation pipeline.

Generated Data

  500 Customers
  3,000 Orders
  Multiple Products
  Campaign Engagement Records

Membership Tiers

Silver
Gold
Platinum

Products

  Espresso
  Latte
  Cappuccino
  Mocha
  Cold Brew
  Americano
  Flat White
  Vanilla Cold Brew
  Hazelnut Latte
  Caramel Latte

---

 Installation

1. Clone Repository

```bash
git clone https://github.com/yourusername/brewmind.git
cd brewmind
```

2. Create Virtual Environment

```bash
python -m venv venv
```

3. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

4. Install Dependencies

```bash
pip install -r requirements.txt
```

5. Configure Database

Update your MySQL credentials inside:

```python
app/database.py
```

Example:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/brewmind"
```

### 6. Run Application

```bash
uvicorn app.main:app --reload
```

API Documentation

After starting the server:

Swagger UI
http://127.0.0.1:8000/docs


Deployment
Backend Hosting: Render
Database Hosting: Railway MySQL


Future Improvements

 JWT Authentication
 Role-Based Access Control (RBAC)
 Redis Caching
 Email Campaign Integration
 SMS Campaign Integration
 Customer Lifetime Value Prediction
 Recommendation Engine
 Kafka Event Streaming
 Real-Time Analytics Dashboard
 AI-Powered Customer Segmentation
