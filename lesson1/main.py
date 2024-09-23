import requests

#what is API?
username = "ThePizzaGuy99"
url = f"https://api.chess.com/pub/player/{username}"\

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers = headers)
print("Status Code:", response.status_code)

player_data = response.json()
print("Username: "+ player_data["username"])