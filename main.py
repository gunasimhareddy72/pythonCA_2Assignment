import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__, template_folder='templates')
app.secret_key = "random random"





if __name__ == '__main__':
    app.run(debug=True)