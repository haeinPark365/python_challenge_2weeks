import requests
import os

def run_day_four():
  i=1
  while(i):
    print("welcome to IsItDown.py!")
    urls = get_url()
    if urls is not None:
      check_url(urls)
    i=start_over()
  

def get_url():
  input_urls = []
  input_urls = input("please write a URL or URLs you want to check. (seperated by comma)\n")
  input_urls = input_urls.strip().replace(" ","").split(",")

  urls = []
  for url in input_urls :
    if url.endswith(".com"):
      if not url.startswith("http://"):
        url = f"http://{url}"
      urls.append(url)
    else:
      print(f"{url} is not a valid URL")
      return 

  return urls


def check_url(urls):
  for url in urls:
    try:
      request = requests.get(url)
      r_code = request.status_code
      if r_code == 200:
        print(f"{url} is up!")
    except :
      print(f"{url} is down!")
      pass
      continue
  return

def start_over():
  while(1):
    i = input("Do you want to start over? y/n ")
    if i=='y':
      os.system('clear')
      return 1
    elif i=='n':
      print("Bye!")
      return 0
    else:
      print("That's not a valid answer")
    
    

 