from flask import Flask
from flask import flash
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from database_setup import Base
from database_setup import MenuItem
from database_setup import Restaurant
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


""" API to get list of restaurants in JSON format.
"""
@app.route('/restaurants/JSON')
def restaurants_json():
    restaurants = session.query(Restaurant).order_by(Restaurant.name).all()
    return jsonify(Restaurant=[restaurant.serialize for restaurant in restaurants])


""" API to get complete menu of a restaurant in JSON format.
"""
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def menu_json(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return jsonify(MenuItems=[item.serialize for item in items])


""" API to get a menu item of a restaurant in JSON format.
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menu_item_json(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=item.serialize)


""" show_restaurants: Show all the restaurants.
"""
@app.route('/')
@app.route('/restaurants/')
def show_restaurants():
    restaurants = session.query(Restaurant).order_by(Restaurant.name)
    return render_template('show_restaurants.html', restaurants=restaurants)


""" new_restaurant: Create new restaurant.
"""
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        if request.form['name']:
            new_restaurant = Restaurant(name=request.form['name'])
            session.add(new_restaurant)
            session.commit()
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('new_restaurant.html')


""" edit_restaurant: Edit a restaurant name.
"""
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    if request.method == 'POST':
        if request.form['name']:
            edited_restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
            edited_restaurant.name = request.form['name']
            session.add(edited_restaurant)
            session.commit()
            flash("Restaurant name has been edited!")
        return redirect(url_for('show_restaurants'))
    else:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        return render_template('edit_restaurant.html',
                               restaurant_name=restaurant.name,
                               restaurant_id=restaurant.id)


""" delete_restaurant: Delete a restaurant.
"""
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    if request.method == 'POST':
        deleted_restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        session.delete(deleted_restaurant)
        session.commit()
        flash("Restaurant has been deleted!")
        return redirect(url_for('show_restaurants'))
    else:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        return render_template('delete_restaurant.html',
                               restaurant_name=restaurant.name,
                               restaurant_id=restaurant.id)


""" show_menu: Show menu of a restaurant.
"""
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('show_menu.html',
                           restaurant_name=restaurant.name,
                           restaurant_id=restaurant.id,
                           items=items)


""" new_menu_item: Create new menu item for a restaurant.

    name, description, price, course (Appetizer, Main, or Dessert)
"""
@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        if request.form['name'] and request.form['description'] and \
           request.form['price'] and request.form['course']:

            new_item = MenuItem(name=request.form['name'],
                                description=request.form['description'],
                                price=request.form['price'],
                                course=request.form['course'],
                                restaurant_id=restaurant_id)
            session.add(new_item)
            session.commit()
            flash("New menu item has been created!")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html', restaurant_id=restaurant_id)


""" edit_menu_item: Edit menu item for a restaurant.
"""
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    if request.method == 'POST':
        if request.form['name']:
            edited_item = session.query(MenuItem).filter_by(id=menu_id).one()
            edited_item.name = request.form['name']
            session.add(edited_item)
            session.commit()
            flash("Menu item has been edited!")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        edited_item = session.query(MenuItem).filter_by(id=menu_id).one()
        return render_template('edit_menu_item.html',
                               restaurant_id=restaurant.id,
                               restaurant_name=restaurant.name,
                               menu_id=edited_item.id,
                               menu_name=edited_item.name)


""" delete_menu_item: Delete menu item for a restaurant.
"""
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    if request.method == 'POST':
        deleted_item = session.query(MenuItem).filter_by(id=menu_id).one()
        session.delete(deleted_item)
        session.commit()
        flash("Menu item has been deleted!")
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        deleted_item = session.query(MenuItem).filter_by(id=menu_id).one()
        return render_template('delete_menu_item.html',
                               restaurant_id=restaurant_id,
                               restaurant_name=restaurant.name,
                               menu_id=deleted_item.id,
                               menu_name=deleted_item.name)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key' # This should be super secret for real apps!
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
