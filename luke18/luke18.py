import csv #https://stackoverflow.com/questions/24662571/python-import-csv-to-list
import numpy as np
import pandas as pd
import math

#key_value = np.loadtxt("luke18/employees.csv", delimiter=",", dtype=str)
#mydict = { k:v for k,v in key_value }
alfabeth = "_ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

SWFirstnames_Male = np.loadtxt("luke18/SWFirstname_Male.txt", dtype=str)
SWFirstnames_Male_Count = len(SWFirstnames_Male)
SWFirstnames_Female = np.loadtxt("luke18/SWFirstname_Female.txt", dtype=str)
SWFirstnames_Female_Count = len(SWFirstnames_Female)
SWLastnames_Part1 = np.loadtxt("luke18/SWLastname_Part1.txt", dtype=str)
SWLastnames_Part1_Count = len(SWLastnames_Part1)
SWLastnames_Part2 = np.loadtxt("luke18/SWLastname_Part2.txt", dtype=str)
SWLastnames_Part2_Count = len(SWLastnames_Part2)

def GetSWName(firstname, lastname, sex):
    SWName = "UNDEFINED"
    ## ASCII-verdien for kvar bokstav i fornamnet blir lagt saman. 
    asciiValueFirstname = 0
    for c in [ord(c) for c in firstname]:
        asciiValueFirstname += c  
    # Denne verdien modulo antall namn i respektivt manne- eller kvinnelista 
    # gir indeksen som brukast for å hente ut fornamn frå riktig liste.
    if (sex == "M"):
        SWFirstname = SWFirstnames_Male[asciiValueFirstname % SWFirstnames_Male_Count]
    if (sex == "F"):
        SWFirstname = SWFirstnames_Female[asciiValueFirstname % SWFirstnames_Female_Count]
    
    # Etternamn delast på 2, der første halvdel blir den lengste i tilfeller der 
    # etternamna har odde antal bokstavar.
    Lastname_Part1 = lastname[:math.ceil(len(lastname)/2)] #slicing and Math
    Lastname_Part1Value = 0
    for i in Lastname_Part1:
        # Posisjonen i alfabetet for kvar bokstav i første halvdel leggast saman. 
        Lastname_Part1Value += alfabeth.find(i.capitalize()) 
    # Denne summen modulo antal element i lista over første del av etternavn blir 
    # indeksen som brukast for å plukke frå denne lista.
    SWLastname_Part1 = SWLastnames_Part1[Lastname_Part1Value % SWLastnames_Part1_Count]

    Lastname_Part2 = lastname[math.ceil(len(lastname)/2):] #slicing and Math
    Lastname_Part2Value = 1
    # ASCII-verdien for kvar bokstav i andre halvdel av etternamnet blir ganga saman. 
    for c in [ord(c) for c in Lastname_Part2]:
        Lastname_Part2Value *= c
    # Dette produktet blir om personen er kvinne ganga med antall bokstavar i heile 
    # namnet. Om personen er mann blir produktet ganga med antall bokstavar i 
    # fornamnet.
    if (sex == "M"):
        Lastname_Part2Value *= len(firstname)
    if (sex == "F"):
        Lastname_Part2Value *= len(firstname + " " + lastname)
    # I det resulterande talet sorterast alle siffera i synkande rekkefølge. 
    Lastname_Part2Value = int("".join(sorted(str(Lastname_Part2Value), reverse=True)))
    # Dette talet modulo antal element i del-to-lista blir indeksen for å hente ut 
    # siste del av starwars-namnet.
    SWLastname_Part2 = SWLastnames_Part2[Lastname_Part2Value % SWLastnames_Part2_Count]
    
    SWName = SWFirstname + " " + SWLastname_Part1 + SWLastname_Part2
    #print("Employee: ", firstname, lastname, sex, "SWName: ", SWName)
    return SWName

employees = pd.read_csv("luke18/employees.csv")
#print(employees)

#for employee in employees:
#    print(GetSWName(employee['firstname'], employee['lastname'], employee['sex']))

# https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/
# iterate through each row and concatenate 
# 'Name' and 'Percentage' column respectively. 
employees.insert(3, 'SWName', "", True)
for i, employee in employees.iterrows():
    employees.at[i,'SWName'] = GetSWName(employee['first_name'], employee['last_name'], employee['gender'])

print(employees)
#https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column/48590361
print("Most used name: ", employees['SWName'].value_counts()[employees['SWName'].value_counts() == employees['SWName'].value_counts().max()])

Testemployee = {
    "firstname": "Jan", 
    "lastname": "Johannsen", 
    "sex":"M" }

assert (GetSWName(Testemployee["firstname"], Testemployee["lastname"], Testemployee["sex"]) == "Poe Lightverse")