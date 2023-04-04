from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(500))


prod_links = {"Pens": "https://m.media-amazon.com/images/I/71OhYdo2p7L._AC_SL1500_.jpg",
              "Pencils": "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T2/images/I/71L9v+sO-dL._AC_SL1500_.jpg",
              "Notebook": "https://poppin.imgix.net/products/2022/Sky_Elements_1_Subject_Notebook_PDP_02.jpg?w=1600&h=1600",
              "Highlighters": "https://cdn.shopify.com/s/files/1/0036/4806/1509/products/dc5382b88514a384e0205a6e6233218436453572_square491714_1_1000x1000.jpg?v=1674694214",
              "Sticky Notes": "https://www.tvmkart.com/wp-content/uploads/2020/07/Sticky-Notes.jpg",
              "Dry Erase Board": "https://dijf55il5e0d1.cloudfront.net/images/na/5/4/1/54118_1000.jpg",
              "Dry Erase Markers": "https://m.media-amazon.com/images/I/81mKJh0tJQL._AC_SX466_.jpg",
              "Calculator": "https://m.media-amazon.com/images/I/7106ob3ATYL._AC_SY355_.jpg",
              "Backpack": "https://m.media-amazon.com/images/I/81LpeKZIFmL._AC_SX466_.jpg",
              "3-Ring Binder": "https://assets.sellers.loblaw.ca/products/all/1139/104891_1.jpg?size=480",
              "Coloured Pencils": "https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/27ED75A034604D72BFADD5D5466E7131/10530697_21.jpg?fit=inside|540:540",
              "12\" Ruler": "https://ajaxscientific.com/wp-content/uploads/MO123-11480.jpg",
              "Glue Stick": "https://static-ppimages.freetls.fastly.net/product/2000055314709-2.jpg?canvas=600,600&fit=bounds&height=600&mode=max&width=600&404=default.jpg",
              "Crayons": "https://p1.pxfuel.com/preview/131/542/380/crayons-close-up-background-colorful-assortment-box.jpg",
              "Stapler": "https://content.etilize.com/400/1023444202.jpg",
              "Scissors": "https://assets.sellers.loblaw.ca/products/all/1276/281734_1.jpg?size=480"
              }

def add_products():
    print("ADDING PRODUCTS!!")
    products = [
        Product(name="Pens", price=3.99, id=1, description="12-Pack, Black", image=prod_links["Pens"]),
        Product(name="Pencils", price=5.99, id=2, description="36-Pack, Number 2", image=prod_links["Pencils"]),
        Product(name="Notebook", price=2.99, id=3, description="200 Pages, Lined", image=prod_links["Notebook"]),
        Product(name="Highlighters", price=4.99, id=4, description="8-Pack, Multicoloured", image=prod_links["Highlighters"]),
        Product(name="Sticky Notes", price=1.99, id=5, description="Small, Yellow", image=prod_links["Sticky Notes"]),
        Product(name="Dry Erase Board", price=19.99, id=6, description="20\" x 36\"", image=prod_links["Dry Erase Board"]),
        Product(name="Dry Erase Markers", price=5.99, id=7, description="4-Pack, Multicoloured", image=prod_links["Dry Erase Markers"]),
        Product(name="Calculator", price=14.99, id=8, description="Standard Scientific Calculator", image=prod_links["Calculator"]),
        Product(name="Backpack", price=24.99, id=9, description="One size fits all, Black", image=prod_links["Backpack"]),
        Product(name="3-Ring Binder", price=3.99, id=10, description="Available in 6 colours", image=prod_links["3-Ring Binder"]),
        Product(name="Coloured Pencils", price=4.99, id=11, description="24-Pack, Multicoloured", image=prod_links["Coloured Pencils"]),
        Product(name="12\" Ruler", price=1.99, id=12, description="Include both Inches and Centimeters", image=prod_links["12\" Ruler"]),
        Product(name="Glue Stick", price=1.99, id=13, description="Solvent Free, 36g", image=prod_links["Glue Stick"]),
        Product(name="Crayons", price=4.99, id=14, description="36-Pack, Multicoloured", image=prod_links["Crayons"]),
        Product(name="Stapler", price=6.99, id=15, description="Standard Size Stapler", image=prod_links["Stapler"]),
        Product(name="Scissors", price=3.99, id=16, description="Available in 4 colours", image=prod_links["Scissors"])
    ]
    for product in products:
        db.session.add(product)
    db.session.commit()

def delete_all_products():
    db.session.query(Product).delete()
    db.session.commit()

@app.route('/get_products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_list.append({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'image': product.image})
    return jsonify({'products': product_list})

# @app.route('/add', methods=['POST'])
# def add_product_to_cart():


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        if not Product.query.first():
            add_products()

        products = Product.query.all()
        for product in products:
            print(product.name, product.price, product.description)
    app.run(debug=True)
