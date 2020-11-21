import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
url_country = "https://www.iban.com/currency-codes"
url_exchange = "https://transferwise.com/gb/currency-converter"

countries = []

def get_countries():
  print("Welcome to CurrencyConvert PRO 2020")

  request = requests.get(url_country)
  soup = BeautifulSoup(request.text, "html.parser")
  table = soup.find("table")
  rows = table.find_all("tr")[1:]

  get_list(rows)

  for index, country in enumerate(countries):
    print(f"# {index} {country['name']} ")
    

  print("\nWhere are you from? Choose a county by number!")
  first = get_ask()

  print("\nNow choose another country.")
  second = get_ask()

  print(f"\nHow many {first} do you want to convert to {second}?")
  num = ''
  while type(num) != int:
    num = get_num()
  input_amount = num

  input_li = {
    'first' : first,
    'second' : second,
    'input_amount' : input_amount
  }

  return input_li
  
    
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


def get_ask():
  try:
    answer = int(input("#: "))
    if answer > len(countries):
      print("Choose a number form the list")
      get_ask()
    else :
      country = countries[answer]
      print(country['name'])
      answer = country['code']

  except:
    print("That was'nt a number")
    get_ask()
  
  return answer

def get_num():
  amount = input()
  try:
    amount=int(amount)
  except:
    print("That was'nt a number")
  
  return amount
  
  

def exchange(li):

  first = li['first']
  second = li['second']
  input_amount = li['input_amount']
  

  request = requests.get(f"{url_exchange}/{first}-to-{second}-rate?amount={input_amount}")
  soup = BeautifulSoup(request.text, "html.parser")
  result = float(soup.find("span",{"class":"text-success"}).text)
  amount = float(input_amount) * result

  print(f"\n{first} {input_amount} is ", end='')
  print(format_currency(amount, second, locale="ko_KR"))

def run_day_six():
  ex_li = get_countries()
  exchange(ex_li)