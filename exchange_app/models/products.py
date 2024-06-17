from app.app_init import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False )
    price_usd = db.Column(db.Float, nullable=False)
    price_pln = db.Column(db.Float)
    last_update = db.Column(db.DateTime, )
