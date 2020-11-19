import requests

def run_day_four():
  URL = "http://www.naver.com"
  request = requests.get(URL)
  print(request.status_code)
