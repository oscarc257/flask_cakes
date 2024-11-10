"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()
        
    
        


class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")

def to_dict(self):
    """Serialize cupcake to a dict of cupcake info."""
    return {
        "id": self.id,
        "flavor": self.flavor,
        "rating": self.rating,
        "size": self.size,
        "image": self.image,
    }          