from project import db,app

#create the Milk_products table
class Milk_products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable= False)
    price = db.Column(db.String(15), nullable= False)
    Description = db.Column (db.String(100), nullable= False)
    img = db.Column(db.String(100), nullable= False)

    # initialise 
    def __init__(self, name, price, Description, img):
        self.name = name
        self.price = price
        self.Description = Description
        self.img =img

