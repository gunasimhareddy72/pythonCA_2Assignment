import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__, template_folder='templates')
app.secret_key = "random random"


conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="guna",
            host="localhost",
            port="5432"
    )
cursor = conn.cursor(cursor_factory=RealDictCursor)

@app.route("/")
def index():
    return render_template("login.html")
@app.route("/index.html")
def index1():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customer(customer_id, first_name, last_name, mail_id, address) VALUES (%s,%s,%s,%s,%s)",
                       (request.form['customerid'], request.form['firstname'], request.form['lastname'], request.form['gmail'], request.form['address']))
        conn.commit()
        return redirect(url_for('home'))
    except Exception as e:
        conn.rollback()
        return "An error occurred: {}".format(str(e))
    finally:
        cursor.close()






if __name__ == '__main__':
    app.run(debug=True)