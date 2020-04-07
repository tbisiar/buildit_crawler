from bs4 import BeautifulSoup
import requests
import re

url = 'https://wiprodigital.com/'
domain_pattern = '^' + url + '*'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

links = content.findAll('a')

def check_domain( uri ):
  match = re.search(domain_pattern, uri)
  if match is None:
    print("Doesn't match: " + uri)
    return False
  else:
    print(uri)
    return True

for link in links:
  href = link.get('href')
  check_domain(href)

