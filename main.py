import psycopg2
import json
from psycopg2.extras import RealDictCursor
from flask import Flask, session, render_template, request, redirect, g, url_for



app = Flask(__name__, template_folder='templates')
app.secret_key = "Find me if you can"

    
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
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM user_table WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.execute("SELECT * FROM customer")
        customer = cursor.fetchall()
        
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            return render_template("adminhome.html",customers=customer)
        else:
            return "Invalid username or password"
    
    return render_template("login.html")

@app.route("/adminhome.html", methods=['GET','POST'])
def adminhome():
    cursor.execute("SELECT * FROM customer")
    customer = cursor.fetchall()
    return render_template('adminhome.html', customers=customer)
@app.route("/index.html")
def index1():
    username = session.get('username')
    cursor.execute("SELECT * FROM product WHERE username = %s", (username,))
    products = cursor.fetchall()

    return render_template("index.html", products=products)

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
            
@app.route("/home.html", methods=['GET','POST'])
def home():
    cursor.execute("SELECT * FROM customer")
    customer = cursor.fetchall()
    return render_template('home.html', customers=customer)
@app.route("/search", methods=['POST'])
def search_customer():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            
            cursor.execute("SELECT * FROM customer WHERE first_name ILIKE %s OR last_name ILIKE %s", (f'%{search_query}%', f'%{search_query}%'))
            search_results = cursor.fetchall()
            return render_template('home.html', customers=search_results)
        else:
          
            return redirect(url_for('home'))
    
    return redirect(url_for('home'))


@app.route("/delete_customer/<customer_id>", methods=['POST'])
def delete_customer(customer_id):
    print("Customer ID:", customer_id)
    try:
        cursor.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
        conn.commit()
        return redirect('/home.html')  
    except Exception as e:
        conn.rollback()
        return "An error occurred: {}".format(str(e))
@app.route("/editcustomer.html")
def editcustomer():
    with open('grocery_items.json') as f:
        data = json.load(f)
        grocery_items = data["items"]
        return render_template('editcustomer.html',grocery_items=grocery_items)

@app.route("/get_customer_details/<customer_id>")
def get_customer_details(customer_id):
     
    cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))

    customer = cursor.fetchone()
    return render_template("editcustomer.html", customer=customer)

@app.route("/edit_customer/<customer_id>", methods=['GET', 'POST'])
def edit_customer(customer_id):
    if request.method == 'POST':
        try:
            first_name = request.form['firstname']
            last_name = request.form['lastname']
            address = request.form['address']
            email_id = request.form['gmail']
            
            cursor.execute("UPDATE customer SET first_name=%s, last_name=%s, mail_id=%s, address=%s WHERE customer_id=%s",
               (first_name, last_name, email_id, address, customer_id))
            conn.commit()
            return redirect(url_for('home'))
        except Exception as e:
            conn.rollback()
            return "An error occurred: {}".format(str(e))
        
@app.route("/searchadmin", methods=['POST'])
def search_Admin_customer():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            
            cursor.execute("SELECT * FROM customer WHERE first_name ILIKE %s OR last_name ILIKE %s", (f'%{search_query}%', f'%{search_query}%'))
            search_results = cursor.fetchall()
            return render_template('adminhome.html', customers=search_results)
        else:
           
            return redirect('adminhome.html')
  
    return redirect('adminhome.html')
@app.route("/edit_customer_admin/<customer_id>", methods=['GET', 'POST'])
def edit_customer_admin(customer_id):
    if request.method == 'POST':
        try:
            first_name = request.form['firstname']
            last_name = request.form['lastname']
            address = request.form['address']
            email_id = request.form['gmail']
            
            cursor.execute("UPDATE customer SET first_name=%s, last_name=%s, mail_id=%s, address=%s WHERE customer_id=%s",
               (first_name, last_name, email_id, address, customer_id))
            conn.commit()
            return redirect(url_for('adminhome'))
        except Exception as e:
            conn.rollback()
            return "An error occurred: {}".format(str(e))
        
@app.route("/get_customer_details_admin/<customer_id>")
def get_customer_details_admin(customer_id):
     
    cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))

    customer = cursor.fetchone()
    return render_template("editcustomeradmin.html", customer=customer)
@app.route("/delete_customer_admin/<customer_id>", methods=['POST'])
def delete_customer_admin(customer_id):
    print("Customer ID:", customer_id)
    try:
        cursor.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
        conn.commit()
        return redirect('/adminhome.html')  
    except Exception as e:
        conn.rollback()
        return "An error occurred: {}".format(str(e))
if __name__ == '_main_':
    app.run(debug=True)