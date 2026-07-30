from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    db = sqlite3.connect("football.db")
    cursor = db.cursor()
    sql = ("""SELECT nation_name, world_cups_won
           FROM nation
           ORDER BY world_cups_won desc
           """)
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html", send_test = results)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    