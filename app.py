from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    db = sqlite3.connect("football.db")
    cursor = db.cursor()
    sql = ("""SELECT nation_name, world_cups_won
           FROM nations
           ORDER BY world_cups_won desc
           """)
    cursor.execute(sql)
    results = cursor.fetchall()
    temp_list = []
    for item in results:
        temp_list.append(item)
        
    return render_template("home.html", send_test = temp_list)


    
@app.route("/players.html", methods=["GET", "POST"])
def players():
    db = sqlite3.connect("football.db")
    cursor = db.cursor()
    
    sql = ("""SELECT player_name, age, nation_id
           FROM players""")
    
    cursor.execute(sql)
    
    results = cursor.fetchall()
    for i in results:
        sql = ("""SELECT nation_name
            FROM nations
            WHERE nation_id = ?""")
        cursor.execute(sql,(i[0][2]))
        country = cursor.fetchall()
        
        sql = """
            SELECT players.player_name, players.age, nations.nation_name
            FROM players
            LEFT JOIN nations ON players.nation_id = nations.nation_id
        """
    
    
    return render_template("players.html", send_player = country)
    
    
    
    
@app.route("/search.html", methods=["GET", "POST"])
def search():
    
    
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug=True)
    