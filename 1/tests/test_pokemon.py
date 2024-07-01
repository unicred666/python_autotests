import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "1e161d092ba584a3045be6da3109a9f1"  # замените на действительный токен вашего тренера
HEADER = {'Content-type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4126'
 
def test_status_code(): # ответ запрос GET /trainers приходит с кодом 200
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response(): #
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]["trainer_name"] == 'Нэш'
