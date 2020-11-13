from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import config
app = Flask(__name__)


app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.username
app.config['MYSQL_PASSWORD'] = config.password
app.config['MYSQL_DB'] = config.db

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        food_name = details['fname']
        quantity = details['quantity']
        quantity_indentifier = details['quantity_indentifier']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Foods(food_name, quantity) VALUES (%s, %s)", (food_name, quantity))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
