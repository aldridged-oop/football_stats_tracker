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
    for item in results:
        temp_list.append(item)
        
    return render_template("index.html", send_test = temp_list)


    
@app.route("/players.html", methods=["GET", "POST"])
def players():
    
    
    return render_template("players.html")
    
    
    
    
@app.route("/search.html", methods=["GET", "POST"])
def search():
    
    
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug=True)
    