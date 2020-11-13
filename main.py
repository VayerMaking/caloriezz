from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from MySQLdb import escape_string as thwart

import config
app = Flask(__name__)


app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.username
app.config['MYSQL_PASSWORD'] = config.password
app.config['MYSQL_DB'] = config.db

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == "POST":
        details = request.form
        food_name = details['fname']
        quantity = details['quantity']
        quantity_indentifier = details['quantity_indentifier']
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO Foods(food_name, quantity, quantity_indentifier) VALUES (%s, %s, %s)", (food_name, quantity, quantity_indentifier))
        cur.execute('''SELECT food_name FROM Foods''')
        rv = cur.fetchall()
        #return str(rv)
        for row in rv:
            print(row[0])
            result.append(row[0])
            result.append("asdf")

        mysql.connection.commit()
        cur.close()
        return result
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
