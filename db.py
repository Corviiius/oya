import sqlite3
from random import shuffle

def get_all_alive():
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    sql = "SELECT user name FROM players"
    data = cursor.execute(sql)
    data = [row[0] for row in data]
    con.commit()
    con.close()
    return data

def set_roles(players):
    game_roles = ['citizen'] * plyers
    mafias = int(players * 0.3)
    for i in range(mafias):
        game_roles[i] = 'mafia'
        shuffle(game_roles)
        con = sqlite3.connect('db.db')
        cur = con.cursor
        cur.execute(f"SELECT player_id FROM PLAYERS")
        player_ids_rows = cur.fetchall()
        for role, row in zip (game_roles, player_ids_row):
            sql = f"UPDATE players SET role = '{role}' WHERE player_id = {row[0]}"
            cur.execute(sql)
        con.commit()
        con.close()

def insert_player(player_id, username):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    sql = f"INSERT INTO players (player_id, username) VALUES ('{player_id}', '{username}')"
    cur.execute(sql)
    con.commit()
    con.close()