#parcial

from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint

#1

pers1 = input ("nombre del primer personaje")
pers2 = input ("nombre del segundo personaje")

altura1 = int(input("altura del primer personaje"))
altura2 = int(input("altura del segundo personaje"))

peso1 = int(input("peso del primer personaje"))
peso2 = int(input("peso del segundo personaje"))

planeta_de_origen1 = int(input("ingrese el planeta de origen del primer personaje: "))
planeta_de_origen2 = int(input("ingrese el planeta de origen del segundo personaje: "))

cantidad_de_peliculas1 = int(input("ingrese la cantidad de peliculas del primer personaje: "))
cantidad_de_peliculas2 = int(input("ingrese la cantidad de peliculas del segundo personaje: "))

pers1 = [pers1,altura1, peso1, planeta_de_origen1, cantidad_de_peliculas1]
pers2 = [pers2,altura2,peso2, planeta_de_origen2, cantidad_de_peliculas2 ]

#A
if(pers1[1] > pers2[1]):
    print(pers1[0],'ES MAS ALTO')
elif(pers1[1] == pers2[1]):
    print("son del mismo tamaño")
else:
    print(pers2[0],'ES MAS Alto')

#B

if (pers1[2] > pers2[2]):
    print (pers1[0], 'es mas pesado')
elif(pers1[2] == pers2[2]):
    print("pesan lo mismo")
else:
    print(pers2[0], 'es el mas pesado ')

#C
if (pers1[4] > pers2[4]):
    print (pers1[0], "participo en mas peliculas")
elif(pers1[4] == pers2[4]):
    print ("participaron la misma cantidad de veces")
else:
    print(pers2[0], "participo en mas peliculas ")

#D

print ("personaje")
if(pers1 == "Yoda" or pers1 == "Chewbacca"):
    print('personaje 1', )
if(pers2 == "Yoda" or pers2 == "Chewbacca"):
    print('personaje 2' )

#2

import json
import requests
from random import randint


def xnombre(item):
    return item["name"]

def get_data(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
        dic= json.loads(req.text)
        return dic

def get_data_sw_characters():
    sw_data = []
    result = get_data("https://swapi.dev/api/people/")
    while(result["next"] is not None):
        for doc in result["results"]:
            sw_data.append(doc)
        result = get_data(result["next"])
    return sw_data

sw_data = get_data_sw_characters()

sw_data.sort(key=xnombre)

print("2.A")
for character in sw_data:
    print(character["name"], character["height"], "cm", len(character["films"]), "peliculas")
print(" 2.B")
for character in sw_data:
    if character["name"].startswith("D" or "C") or character["name"].endswith("s"):
        print(character["name"])

#3
from random import randint, random


lista = []

for i in range(77):
    lista.append(randint(1, 100))

lista.sort()

print('menor', lista[0])
print('mayor', lista[-1])


print ( 'diferencia entre menor y mayor', lista[0] -  lista[-1])

print('listado creciente')
for num in lista:
    print(num)


lista.sort(reverse=1)



print('listado decreciente')

for num in lista:
     print(num)

print('impares que no son multiplos de 3')
for num in lista:
    if(num % 3 > 0 and num % 2 > 0):
        print(num)

print ("promedio")
print(sum(lista) / 100)







































































































































