import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

countries = []

def run_day_five():
  print("Hello! please choose select a county by number!")

  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  table = soup.find("table")
  rows = table.find_all("tr")[1:]

  get_list(rows)

  for index, country in enumerate(countries):
    print(f"# {index} {country['name']} ")
    
  get_num()
  return 
  
    
def get_list(rows):
  for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    
    if(name and code):
      country = {
        'name': name.capitalize(),
        'code': code
      }
      countries.append(country)


def get_num():
  try:
    answer = int(input("#: "))
    if answer > len(countries):
      print("Choose a number form the list")
      get_num()
    else :
      country = countries[answer]
      print(f"The currency code is {country['code']}")

  except:
    print("That was'nt a number")
    get_num()
  


