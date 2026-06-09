import requests

headers = {
    'x-api-key': 'pub_2998cecfc24fcd213346d4656783907ff4f1c9290c3762a2e83082fdf1068864'
}

def test_APIUS01_obtener_usuario():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    print (response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 2 #menos de dos segundos

def test_APIUS02_crear_usuario():
    body = {
        "name": "juancho",
        "email": "aghiazzabna@gmail.com",
        "password": "12345",
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json()

    assert response.status_code == 201, "No se pudo crear el usuario."
    assert data["name"] == body["name"], "El nombre no se generó correctamente."
    assert data["email"] == body["email"], "El email no se generó correctamente."
    assert data["password"] == body["password"], "La contraseña no se generó correctamente."

def test_APIUS03_eliminar_usuario():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204