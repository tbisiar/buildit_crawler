import unittest
from crawler import Crawler

class TestCrawlerMethods(unittest.TestCase):
  def test_check_link(self):
    res = Crawler.crawl("asdf")
    self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()