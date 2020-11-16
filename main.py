from flask import Flask, render_template, request, flash, redirect, url_for
#from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

import config
app = Flask(__name__)


app.config['SECRET_KEY'] = config.password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(config.username, config.password, config.host, config.dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class foods(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    food_name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    quantity_indentifier = db.Column(db.Enum('kg', 'mg', 'number'))
    calories = db.Column(db.Integer())

    def __init__(self, food_name, category, quantity_indentifier, calories):
        self.food_name = food_name
        self.category = category
        self.quantity_indentifier = quantity_indentifier
        self.calories = calories

def calc(calories, quantity):
    return calories * quantity

def check_food_name(food_name, category, quantity):
    data = foods.query.filter_by(food_name=food_name, category=category).first()
    calories = data.calories
    return calories * quantity

'''def check_food_name2(food_name, quantity):
    result = 0
    data = foods.query.all()
    for i in data:
        if(food_name == i.food_name):
            print(i.food_name)
            print(quantity)
            print(i.calories)
            #calculation of calories using quantity and calories for one piece
            #...
            #

            #result = i.calories * quantity
            #return result
            return calc(i.calories, quantity)
    #return result'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == "POST":
        details = request.form
        food_name = details['fname']
        category = details['category']
        quantity = int(details['quantity'])
        quantity_indentifier = details['quantity_indentifier']
        #result  = food_name + quantity_indentifier + str(quantity)
        #return result
        #return redirect(url_for('result', result_out=result_out))
        result = check_food_name(food_name, category, quantity)
    return render_template('index.html', result=result)
'''
@app.route('/result/<result_out>')
def result(result_out):
    return render_template('result.html', result_out=result_out)
'''
@app.route('/asdf', methods=['GET', 'POST'])
def asdf():
    data = foods.query.all()
    for i in data:
        if(i.food_name == "Eggs"):
            print(i.food_name)
            result = i.food_name + i.quantity_indentifier + str(i.calories)
    return result

if __name__ == '__main__':
    app.run(debug=True)
