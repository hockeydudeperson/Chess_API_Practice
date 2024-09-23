import requests
from helper import *

def top_games_of_month(username, year, month):
    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    wins = []
    for game in games:
        #if user is playing as white
        if game["white"]["username"].lower() == username.lower():
            #if result for white is a win
            if game["white"]["result"] == "win":
                black_rating = game["black"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": black_rating
                }
                wins.append(new_game)

        elif game["black"]["username"].lower() == username.lower():
            #if result for black is a win
            if game["black"]["result"] == "win":
                white_rating = game["white"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": white_rating
                }
                wins.append(new_game)
    wins = sorted(wins, key=lambda x: x["opp_rating"], reverse = True)
    top_10_wins = wins[:10]
    counter = 1
    for win in top_10_wins:
        game = win["game"]
        opp_rating = win["opp_rating"]
        url = game["url"]

        print(f"{counter}. url: {url}")
        print(f"opponent_rating: {opp_rating}")
        print()
        counter = counter+1

top_games_of_month("hikaru", "2024/09")