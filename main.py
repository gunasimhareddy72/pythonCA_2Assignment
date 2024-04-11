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
     with open('grocery_items.json') as f:
        data = json.load(f)
        grocery_items = data["items"]
        return render_template("index.html",grocery_items=grocery_items)

@app.route("/submit", methods=['POST'])
def submit():
    
    
   try:
        
        customer_id = request.form['customerid']
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['gmail']
        address = request.form['address']
        gecrios_list = request.form.getlist('grocery_items[]')  

        
        cursor.execute("INSERT INTO customer (customer_id, first_name, last_name, mail_id, address, gecrios_list) VALUES (%s, %s, %s, %s, %s, %s)",
                       (customer_id, first_name, last_name, email, address, gecrios_list))
        conn.commit()

        return redirect(url_for('home'))
   except Exception as e:
        conn.rollback()
        return "An error occurred: {}".format(str(e))






if __name__ == '__main__':
    app.run(debug=True)