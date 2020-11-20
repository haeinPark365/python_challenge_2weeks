import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def run_day_five():
  print("Hello! please choose select a county by number!")

  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  table = soup.find("table",{"class":"table table-bordered downloads tablesorter"}).find("tbody")
  tr = table.find_all("tr")

  lis = get_list(tr)
  get_num(lis)
  return 
  
    
def get_list(tr):
  lis = []
  for r in tr:
    d = r.find_all("td")
    li=[]
    for i in range(len(d)):
      if(i==1 or i==3):
        continue

      s = str(d[i]).replace("<td>","").replace("</td>","")
      if s != '':
        li.append(s)
      else:
        continue
    
    lis.append(li)
    for i in range(len(lis)):
      if len(lis[i]) != 2:
        del lis[i]
  
  for index, value in enumerate(lis):
    print(f"# {index} {value[0]} ")

  return lis


def get_num(lis):
  answer = input("#: ")
  try:
    answer = int(answer)
  except:
    pass
  if type(answer) == int:
    if answer>=0 and answer<len(lis):
      print(f"The currency code is {lis[answer][1]}")
    else:
      print("Choose a number form the list")
      get_num(lis)
  else:
    print("That was'nt a number")
    get_num(lis)


