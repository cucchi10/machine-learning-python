import random
from random import choice

alumnos=['a', 'e', 'i', 'o', 'u']

alumnas=['b', 'c', 'd', 'f', 'g']

print(choice(alumnos + alumnas))


palabra=choice(alumnos) + choice(alumnos) + choice(alumnos) + choice(alumnos)

print(palabra)

