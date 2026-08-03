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
    temp_list = []
    for tuple in results:
        for item in tuple:
            temp_list.append(item)
        
    return render_template("index.html", send_test = temp_list)

if __name__ == "__main__":
    app.run(debug=True)
    
    
        