# crawler.py

from bs4 import BeautifulSoup
import logging
from logging.config import fileConfig
import requests
import re

fileConfig('log_config.ini')
logger = logging.getLogger()


class Crawler:

  def __init__(self, domain):
    # starting by pointing to http, can handle redirect to https
    self.uri = 'http://' + domain.lower()
    self.domain_pattern = '^https?://' + domain.lower() + '/*'


  def crawl(self):
    response = requests.get(self.uri, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    links = content.findAll('a')
    for link in links:
      href = link.get('href')
      isMatch = self.check_domain(href)
      isMatchString = "+ " if isMatch else "- " 
      logger.debug(isMatchString + href)


  def check_domain(self, href):
    match = re.search(self.domain_pattern, href)
    return not match is None






def main():
  domain = 'wiProdigital.com'
  Crawler(domain).crawl()


if __name__ == "__main__":
  main()