#!/usr/bin/python
# app.py

import sys, getopt
from src.crawler import Crawler
import logging
from logging.config import fileConfig


fileConfig('log_config.ini')
logger = logging.getLogger()

def main(argv):
  domain = ''
  try:
    opts, args = getopt.getopt(argv,"hd:",["domain="])
  except getopt.GetoptError:
    print('app.py -d <domain>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
        print('app.py -d <domain>')
        sys.exit()
    elif opt in ("-d", "--domain"):
        domain = arg
  max_depth = 3
  site_map_set = Crawler(domain, max_depth).crawl(0)
  logger.info('site map:')
  for endpoint in site_map_set:
    logger.info(endpoint)



if __name__ == '__main__':
  main(sys.argv[1:])