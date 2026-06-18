⚡ Quick Start Guide
---
---
1. Install Dependencies
---
Ensure you have Python installed and your virtual environment activated. Install the required packages:

Bash
pip install -r requirements.txt

2. Run the Automated Tests
---
Before launching the server, verify the API endpoints and model integration are functioning properly by running the test suite:

Bash
python -m pytest tests/test_api.py -v

3. Launch the Live Server
---
Start the Uvicorn server to host the API locally:

Bash
uvicorn app.main:app --reload

4. Test the Interactive API
---
Once the server is running, FastAPI automatically generates an interactive Swagger UI.

Open your browser and navigate to: http://127.0.0.1:8000/docs

Expand the POST /predict endpoint.

Click "Try it out", enter a customer JSON payload, and click Execute to receive a live churn prediction.

you can try this one too:
---

{
  "city_tier": "Tier 1",
  "age_group": "25-34",
  "acquisition_channel": "Google Search",
  "loyalty_tier": "Not Enrolled",
  "preferred_category": "Baby Care",
  "skin_type": "Unknown",
  "marketing_consent": 1,
  "recency_days": 26,
  "frequency_180d": 1,
  "monetary_180d": 450.00,
  "return_rate_180d": 0.0,
  "avg_discount_pct_180d": 0.15,
  "avg_rating_180d": 3.0,
  "category_diversity_180d": 1,
  "ticket_count_90d": 0,
  "negative_ticket_rate_90d": 0.0,
  "avg_resolution_hours_90d": 0.0,
  "days_since_signup": 30,
  "sessions_30d": 1,
  "product_views_30d": 2,
  "cart_adds_30d": 0,
  "wishlist_adds_30d": 0,
  "abandoned_carts_30d": 0,
  "email_opens_30d": 0,
  "campaign_clicks_30d": 0,
  "last_visit_days_ago": 26
}