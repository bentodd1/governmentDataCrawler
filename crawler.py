import requests
from bs4 import BeautifulSoup
from models import CareerProjection
page = requests.get('https://data.bls.gov/projections/occupationProj')
soup = BeautifulSoup(page.text, 'html.parser')
from config import db

def toFloat(column):
   return float(column.text.replace(',','').replace('$','').replace('N/A','0').replace('>=',''))
#print(len(soup))
myTable = soup.find("table", {"id": "mytable"})
#tr = mytable.findAll("tr",{"class":"otherStatistics_table_alternateRow statistics_cellrightborder"})
#print(mytable.tbody)

rows = myTable.findAll('tr')
for row in rows[3:]:
    columns = row.find_all('td')

    columList = list(columns)
    if len(columList) !=0:
      myColumn = columList[0].text
      print(myColumn)
      '''print myColumn
      print 'before'
      print columList[2].text
      print 'after'
      print toFloat(columList[2])
      '''
      career = CareerProjection(occupation_title =columList[0].text[0:30],
      soc_code = columList[1].text,
      employment_2016_thousands = toFloat(columList[2]),
      employment_2026_thousands = toFloat(columList[3]),
      employment_change_thousands_2026 = toFloat(columList[4]),
      employment_change_percent_2026 = toFloat(columList[5]),
      openings = toFloat(columList[6]),
      median_wage = toFloat(columList[7]),
      entry_level_education = columList[8].text,
      work_experience_related = columList[9].text,
      on_the_job_training = columList[10].text)
      db.session.add(career)
      db.session.commit()
   # soup2 = BeautifulSoup(dataPiece, 'html.parser')
   # td_list = soup2.find_all("td")
   # print(len(td_list))