# main.py
from sqlalchemy.orm import sessionmaker
from model import Customer, Restaurant, Review
from data import Session

# Create a session
session = Session()

# Print count of customers, restaurants, and reviews
print("Number of customers:", session.query(Customer).count())
print("Number of restaurants:", session.query(Restaurant).count())
print("Number of reviews:", session.query(Review).count())

# Querying and printing customer name
customer = session.query(Customer).filter(Customer.name.ilike("Alice")).first()
if customer:
    print("Customer found:", customer.name)
else:
    print("Customer not found")

# Querying and printing restaurant name
restaurant = session.query(Restaurant).filter(Restaurant.name.ilike("Burger King")).first()
if restaurant:
    print("Restaurant found:", restaurant.name)
else:
    print("Restaurant not found")

# Querying and printing review information
review = session.query(Review).filter_by(rating=5).first()
if review:
    print("Review found:", review.full_review())
else:
    print("Review not found")
