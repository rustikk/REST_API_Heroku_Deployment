from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    #precision is the number of digits to the right of the decimal place
    price = db.Column(db.Float(precision=2))

    #the store by id cant be deleted because it links to the item in that store
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #find the store by the store id
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        #returns the first row where the name queryed for is equal to that name in the database
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
