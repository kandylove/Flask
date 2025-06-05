from flask import Flask, render_template, jsonify
import sqlite3
app = Flask(__name__)
import pandas as pd
import os

APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/api')  # <- this is your new route
def api():
    return jsonify(x=42)

@app.route("/players/count")
def players_count():
    conn = sqlite3.connect("players_20.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchone()[0]
    conn.close()
    return jsonify(count=count)

@app.route("/getData/<int:year>")
def getData(year):
    # Load the CSV file from the static folder, inside the current path
    revenue = pd.read_csv(os.path.join(APP_FOLDER,"static/data/1_Revenues.csv"))

    if year < 1942 or year > 2008:
        return "Error in the year range"

    filteredRevenue = revenue[revenue['Year4']==year][["Name","Year4", "Total Revenue","Population (000)"]]

    # show the post with the given id, the id is an integer
    return filteredRevenue.to_json(orient='records')
