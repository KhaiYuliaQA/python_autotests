import requests

url = "https://api.pokemonbattle.ru/v2"
token = "6560eb5da589df8bc1886799f3c3aaeb"
header = {"Content-Type": "application/json", "trainer_token":token}
body_create = {
    "name": "Maksik",
    "photo_id": 59
}

body_change = {
    "pokemon_id": "66889",
    "name": "Kiskam",
    "photo_id": 59
}

body_add = {
    "pokemon_id": "66889"
}

"""respons_create=requests.post(url=f"{url}/pokemons", headers=header, json=body_create)
print(respons_create.text)"""

respons_change=requests.put(url=f"{url}/pokemons", headers=header, json=body_change)
print(respons_change.text)

respons_add=requests.post(url=f"{url}/trainers/add_pokeball", headers=header, json=body_add)
print(respons_add.text)