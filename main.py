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






if __name__ == '__main__':
    app.run(debug=True)