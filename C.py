import json
import xml.etree.cElementTree as et
import pandas as pd

f = open('covid_cases.json')
covidjson = json.load(f)
x = 0
dateRep = []
countriesAndTerritories = []
cases = []
deaths = []

for i in covidjson['records']:
    dateRep.append(i['dateRep'])
    countriesAndTerritories.append(i['countriesAndTerritories'])
    cases.append(i['cases'])
    deaths.append(i['deaths'])
    x+=1
data = {
    'dateRep':dateRep,
    'countriesAndTerritories':countriesAndTerritories,
    'cases':cases,
    'deaths':deaths
}
df = pd.DataFrame(data)
df.to_csv('C.csv')
print(df)

