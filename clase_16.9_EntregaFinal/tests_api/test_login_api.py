import requests
from utils.api_utils import BASE_URL, HEADERS

def test_APILO01_login_exitoso():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }

    response = requests.post(BASE_URL+"/api/login", headers=HEADERS, json=body)

    assert response.status_code == 200, "El login falló"



def test_APILO02_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post(BASE_URL+"/api/login", headers=HEADERS, json=body)

    assert response.status_code == 400, "Se devolvió Status Code distinto de 400"
