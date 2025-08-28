from fastapi import FastAPI

app = FastAPI()

players = [
    {"id": 1, "name": "Shohei Ohtani", "team": "Dodgers"},
    {"id": 2, "name": "Aaron Judge", "team": "Yankees"},
    {"id": 3, "name": "Mookie Betts", "team": "Dodgers"},
    {"id": 4, "name": "Christian Yelich", "team": "Brewers"}
]

@app.get("/players")
def get_players():
    return players

@app.get("/players/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player
    return ("Cannot find player")