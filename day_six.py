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


def run_day_six():
  print("Welcome to CurrencyConvert PRO 2020")
  input_li = get_countries()
  exchange(input_li)


def get_countries():

  request = requests.get(url_country)
  soup = BeautifulSoup(request.text, "html.parser")
  table = soup.find("table")
  rows = table.find_all("tr")[1:]

  get_list(rows)

  for index, country in enumerate(countries):
    print(f"# {index} {country['name']} ")
    

  first = ask_country("\nWhere are you from? Choose a county by number!")
  second = ask_country("\nNow choose another country.") 

  first_code = first['code']
  second_code = second['code']
  input_amount = ask_amount(first_code, second_code)

  return first_code, second_code, input_amount
  
    
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


def ask_country(text):
  print(text)
  try:
    answer = int(input("#: "))
    if answer > len(countries):
      print("Choose a number form the list")
      return ask_country(text)
    else :
      print(countries[answer]['name'])
      return countries[answer]
  except:
    print("That was'nt a number")
    return ask_country(text)


def ask_amount(first, second):
  print(f"\nHow many {first} do you want to convert to {second}?")
  try:
    amount = int(input())
    return amount
  except:
    print("That was'nt a number")
    return ask_amount(first, second)
  
  

def exchange(li):
  first = li[0]
  second = li[1]
  input_amount = li[2]
  
  request = requests.get(f"{url_exchange}/{first}-to-{second}-rate?amount={input_amount}")
  soup = BeautifulSoup(request.text, "html.parser")
  result = float(soup.find("span",{"class":"text-success"}).text)
  amount = float(input_amount) * result

  first_amount = format_currency(input_amount, first, locale="ko_KR")
  second_amount = format_currency(amount, second, locale="ko_KR")

  print(f"\n{first_amount} is {second_amount}")



