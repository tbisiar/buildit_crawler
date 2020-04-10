#!/usr/bin/python
# app.py

import sys, getopt
from src.crawler import Crawler


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
  Crawler(domain).crawl()



if __name__ == '__main__':
  main(sys.argv[1:])