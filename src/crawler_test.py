import unittest
import crawler

class TestCrawlerMethods(unittest.TestCase):
  def test_check_link(self):
    res = crawler.check_domain("asdf")
    self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()