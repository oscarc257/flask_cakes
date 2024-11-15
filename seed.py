from app import app
from models import db, Cupcake

# Set up application context for database operations
with app.app_context():
    db.create_all()  # Create tables if not existing

    # Define new cupcake instances
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    # Add and commit instances to the database
    db.session.add_all([c1, c2])
    db.session.commit()
