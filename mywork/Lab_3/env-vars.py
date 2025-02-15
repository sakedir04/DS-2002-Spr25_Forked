#!/usr/bin/python3

import os

os.environ["FAV_FLAVOR"] = input('What is your favorite flavor? ')
os.environ["AGE"] = input('What is your age? ')
os.environ["UVA_FIRST_YEAR"] = input('Are you a first-year student at UVA? ')

print("Favorite Flavor:", os.getenv("FAV_FLAVOR"))
print("Age:", os.getenv("AGE"))
print("Is First-Year at UVA:", os.getenv("UVA_FIRST_YEAR"))