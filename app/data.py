# data.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Base, Customer, Restaurant, Review

engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Create a session and add some sample data
session = Session()

# Sample data
sample_customer = Customer(name="Alice")
sample_restaurant = Restaurant(name="Burger King")
sample_review = Review(rating=5, comments="Great food!")

# Add sample data to the session and commit to the database
session.add_all([sample_customer, sample_restaurant, sample_review])
session.commit()
