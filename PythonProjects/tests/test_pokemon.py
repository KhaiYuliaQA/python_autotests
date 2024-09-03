import requests
import pytest

url = "https://api.pokemonbattle.ru/v2"
token = "6560eb5da589df8bc1886799f3c3aaeb"
header = {"Content-Type": "application/json", "trainer_token":token}
TRAINER = "5243"
NAME = "Miskam"

def test_status_code():
    response = requests.get(url = f"{url}/pokemons", params = {"trainer_id" : TRAINER})
    assert response.status_code == 200

def test_name_of_trainer():
    response_get = requests.get(url = f"{url}/trainers", params = {"trainer_id" : TRAINER})
    assert response_get.json()["data"][0]["trainer_name"] == "Miskam"