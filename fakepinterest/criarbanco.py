from fakepinterest import database
from instance import app

with app.app_context():
    database.create_all()