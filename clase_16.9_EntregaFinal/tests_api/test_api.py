import requests

headers = {
    'x-api-key': 'pub_2998cecfc24fcd213346d4656783907ff4f1c9290c3762a2e83082fdf1068864'
}

def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200, "El login falló"



def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 400, "Se devolvió Status Code distinto de 400"


def test_crear_usuario():
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

def test_eliminar_usuario():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204

def test_obtener_usuario():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    print (response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 2 #menos de dos segundos




'''
body = {
    "name": "Adrian",
    "job": "Astronaut"
}

#response = requests.get("https://reqres.in/api/users?page=2", headers=headers)
response = requests.post("https://reqres.in/api/users", headers=headers, json=body) #Pasa el body definido anteriormente

print(response.status_code) #trae el status code
print(response.json()) #.json accede al cuerpo del mensaje

# Post es para crear un nuevo registro
## body = {"name": "Adrian", "job": "Astronaut"}
## response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

# Put es para actualizar el registro por completo
## body = {"name": "Fernando", "job": "Stunt Driver"}
## response = requests.put("https://reqres.in/api/users/2", headers=headers, json=body)

# # Patch es para modificar parte del registro
## body = {"name": "Carlos"}
## response = requests.patch("https://reqres.in/api/users/2", headers=headers, json=body)

# Delete elimina un registro entero
## response = requests.post("https://reqres.in/api/users/2", headers=headers, json=body)
'''