import csv
import json

def read_users_csv():
    with open ("data/users.csv", newline="") as file: #newline evita las lineas vacias
        reader = csv.DictReader(file)  #DictReader guarda cada linea como si fuera un diccionario
        return list(reader)     #
    
