# import sys
# sys.path.append("..")

import unittest
from src.crawler import Crawler

class TestCrawlerMethods(unittest.TestCase):

  def setUp(self):
    self.crawler = Crawler("asdf")

  def test_check_link(self):
    res = self.crawler.check_domain("ghjk")
    self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()