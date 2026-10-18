from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    db = sqlite3.connect("football.db")
    cursor = db.cursor()
    sql = ("""SELECT nation_name, world_cups_won
           FROM nations
           ORDER BY world_cups_won desc, nation_name asc
           """)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    home_list = []
    for item in results:
        home_list.append(item)
        
    return render_template("home.html", send_home = home_list)


    
@app.route("/players.html", methods=["GET", "POST"])
def players():
    db = sqlite3.connect("football.db")
    cursor = db.cursor()   
    sql = ("""SELECT players.player_name, players.age, nations.nation_name
            FROM players
            LEFT JOIN nations ON players.nation_id = nations.nation_id
            """)
    cursor.execute(sql)
    player = cursor.fetchall()
    db.close()
    
    return render_template("players.html", send_player = player)
    
    
    
    
@app.route("/search.html", methods=["GET", "POST"])
def search():
    search_name = request.form.get("player_name", "")
    results = []

    if search_name:
        db = sqlite3.connect("football.db")
        cursor = db.cursor()
        sql = ("""SELECT player_name 
               FROM players 
               WHERE player_name = ?
               """)
        cursor.execute(sql, (search_name,))
        results = cursor.fetchall()
        db.close()

    return render_template("search.html", results = results, search_name = search_name)



if __name__ == "__main__":
    app.run(debug=True)