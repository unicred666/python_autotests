import requests
import random
import string

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "1e161d092ba584a3045be6da3109a9f1"  # замените на действительный токен вашего тренера
HEADER = {'Content-type': 'application/json', 'trainer_token':TOKEN}

# Функция для генерации случайного идентификатора фото
def generate_random_photo_id(min_id=1, max_id=100):
    return random.randint(min_id, max_id)

body_create = {
    "name": "generate",
    "photo_id": generate_random_photo_id()
}

response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json=body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

print(pokemon_id)

body_edit =  {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": generate_random_photo_id()
}

response_edit = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=body_edit)
print(response_edit.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id 
}
response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=body_add_pokeball)
print(response_add_pokeball.text)
