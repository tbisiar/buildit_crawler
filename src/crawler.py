# crawler.py

from bs4 import BeautifulSoup as bs
import logging
from logging.config import fileConfig
import requests
import re

fileConfig('log_config.ini')
logger = logging.getLogger()

# Global variable to hold all the hrefs that have been visited
href_set = set()
HTTP_REGEX = '^(http|https)://'


class Crawler:

  def __init__(self, domain, max_depth):
    # starting by pointing to http, can handle redirect to https
    self.uri = 'http://' + domain.lower()
    self.domain_pattern = HTTP_REGEX + domain.lower() + '*'
    self.max_depth = max_depth

  def crawl(self, current_depth):
    # break if exceeding max depth
    if current_depth > self.max_depth:
      return 
    # otherwise continue to drill down
    response = requests.get(self.uri, timeout=5)
    content = bs(response.content, 'html.parser')
    links = content.findAll('a')
    for link in links:
      check_link(link, self.domain_pattern, current_depth, self.max_depth)
    return sorted(href_set)


def check_link(link, domain_pattern, current_depth, max_depth):
  href = link.get('href')
  is_match = check_domain(href, domain_pattern)
  is_already_visited = check_already_visited(href)
  log_link_info(is_match, is_already_visited, current_depth, href)
  if is_match:
    log_link_info(is_match, is_already_visited, current_depth, href)
    if not check_already_visited(href):
      trimmed_href = re.sub(HTTP_REGEX, '', href)
      Crawler(trimmed_href, max_depth).crawl(current_depth+1)

def check_domain(uri, domain_pattern):
  match_pattern = re.search(domain_pattern, uri)
  return match_pattern is not None

def check_already_visited(uri):
  initial_size = len(href_set)
  href_set.add(uri)
  return len(href_set) == initial_size

def log_link_info(is_match, is_already_visited, current_depth, href):
  is_match_string = ' +  |   ' if is_match else ' -  |   ' 
  has_visited = 'Y    | ' if is_already_visited else 'N    | '
  logger.debug(is_match_string + str(current_depth) + '   |    ' + has_visited + href)






def main():
  domain = 'wiprodigital.com'
  logger.debug('+/- | depth | visited | href')
  max_depth = 2
  site_map_set = Crawler(domain, max_depth).crawl(1)
  logger.info('site map:')
  for href in site_map_set:
    logger.info(href)


if __name__ == '__main__':
  main()