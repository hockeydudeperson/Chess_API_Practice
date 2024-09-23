import requests
import datetime

def display_profile(username):
    url = f"https://api.chess.com/pub/player/{username}"\

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
}

    response = requests.get(url, headers = headers)

    player_data = response.json()
        
    country_url = player_data.get("country")
    country_response = requests.get(country_url, headers = headers)
    country_data = country_response.json()
    country_name = country_data.get("name")
    country_code = country_data.get("code")
    print(f"Country: {country_name}({country_code})")

    print(f"Username: {player_data.get("username", "N/A")}")
    print(f"Url: {player_data.get("url", "N/A")}")
    print(f"Followers: {player_data.get("followers", "N/A")}")
    print(f"Country: {player_data.get("country", "N/A")}")
    # print(f"Last Online: {player_data.get("last_online", "N/A")}")
    last_online = datetime.datetime.fromtimestamp(player_data['last_online']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Last Online: {last_online}")
    joined = datetime.datetime.fromtimestamp(player_data['joined']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Joined: {joined}")
    print(f"Streamer: {player_data.get("is_streamer", "N/A")}")
    print(f"Verified: {player_data.get("verified", "N/A")}")
    print(f"Status: {player_data.get("status", "N/A")}")
    print(f"Username: {player_data.get("username", "N/A")}")
    print(f"League: {player_data.get("league", "N/A")}")
    print(f"Streaming Platforms: {player_data.get("streaming_platforms", "N/A")}")

# display_profile("thepizzaguy99")

def best_win_of_month(username, date):
    url = f"https://api.chess.com/pub/player/{username}/games/{date}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
}
    response = requests.get(url, headers = headers)
    data = response.json()
    games = data.get("games")
    # print(games)

    best_win = None
    best_rating = 99

    for game in games:
        #if username is played as white
        if game["white"]["username"].lower() == username.lower():
            #if result for white is a win
            if game["white"]["result"] == "win":
                #if rating of blackis higher than best rating
                if game["white"]["result"] == "win":
                    best_rating = game["black"]["rating"]
                    best_win = game

        elif game["black"]["username"].lower() == username.lower():
            #if result for black is a win
            if game["black"]["result"] == win:
                #if rating of white is higher than best rating
                if game["white"]["result"] == "win":
                    best_rating = game["white"]["rating"]
                    best_win = game

    if best_win:
        print(f"url: {best_win['url']}")
        print(f"rated: {best_win["rated"]}")

def top_games_of_month(username, date):
    url = f"https://api.chess.com/pub/player/{username}/games/{date}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
}
    response = requests.get(url, headers = headers)
    data = response.json()
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
# best_win_of_month("ThePizzaGuy99", "2024/04")