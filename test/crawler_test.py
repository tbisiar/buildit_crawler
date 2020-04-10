# import sys
# sys.path.append("..")

import unittest
import src.crawler as crawler

class TestCrawlerMethods(unittest.TestCase):

  def setUp(self):
    self.domain_pattern = crawler.HTTP_REGEX + "asdf.com" + '*'

##### check_domain tests
  def test_check_domain_succeeds(self):
    res = crawler.check_domain("https://asdf.com/asdfasdf", self.domain_pattern)
    self.assertEqual(res, True)

  def test_check_domain_fails_regex(self):
    res = crawler.check_domain("ghjk", self.domain_pattern)
    self.assertEqual(res, False)

  def test_check_domain_fails_with_intermediate_string(self):
    res = crawler.check_domain("https://www.facebook.com/asdf/", self.domain_pattern)
    self.assertEqual(res, False)

##### check_link tests
##### TBD


##### check_already_visited tests
##### TBD



if __name__ == '__main__':
    unittest.main()