from app import app
from db import db

db.init_app(app)

#create the database with SQLAlchemy before a request is made to the API
#before_first will only run once which is whats needed since you only want to create a database once
@app.before_first_request
def create_tables():
    db.create_all()