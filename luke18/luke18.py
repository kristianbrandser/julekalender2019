import csv #https://stackoverflow.com/questions/24662571/python-import-csv-to-list
import numpy as np
import pandas as pd

#key_value = np.loadtxt("luke18/employees.csv", delimiter=",", dtype=str)
#mydict = { k:v for k,v in key_value }

employees = pd.read_csv("luke18/employees.csv")
print(employees)

def GetSWName(firstname, lastname, sex):
    print(firstname, lastname, sex)
    return "UNDEFINED"

Testemployee = {
    "firstname": "Jan", 
    "lastname": "Johannsen", 
    "sex":"M" }

GetSWName(Testemployee["firstname"], Testemployee["lastname"], Testemployee["sex"])

## Jan = 74 + 97 + 110 = 281
# 281 % 36 = 29. Plass 29 i lista over mannsnamn (nullindeksert) = Poe
# Johannsen -> Johan, nsen
# Alfabetverdiane (a = 1, b = 2 osv) av Johan = 10, 15, 8, 1, 14, som summert blir 48. 48 % 24 = 0. Indeks 0 i lista = Light
# ASCII-verdiane av nsen = 110, 115, 101, 110. Produktet av desse blir 140541500. Ganga med 3 blir det 421624500.
# 421624500 sortert blir 654422100. 654422100 modulo 26 = 20. Indeks 20 gir verse
# Jan Johannsen blir dermed Poe Lightverse.