import requests

headers = {
    'x-api-key': 'pub_2998cecfc24fcd213346d4656783907ff4f1c9290c3762a2e83082fdf1068864'
}

def test_APILO01_login_exitoso():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200, "El login falló"



def test_APILO02_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 400, "Se devolvió Status Code distinto de 400"
