from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "h8ers"
api = Api(app)

#create the database with SQLAlchemy before a request is made to the API
#before_first will only run once which is whats needed since you only want to create a database once
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)          #/auth

#adding the resource and determining how its going to be called
#<string:name> inputs directly into the get method's parameter
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:3200/item/item-name
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=3200, debug=True)