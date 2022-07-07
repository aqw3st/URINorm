import unittest
from urinorm import URINorm

class URINormTest(unittest.TestCase):
  # def test_to_punycode(self):
  #   uri = URINorm('http://тест.рф').to_punycode()
  #   punycode_uri = 'http://xn--e1aybc.xn--p1ai'
  #   self.assertEqual(uri, punycode_uri)

  def test_remove_dot_segments(self):
    uri1 = URINorm('https://www.test.com/../a/b/../c/./d.html').remove_dot_segments()
    uri2 = URINorm('http://google.com/mid/content=5/../6').remove_dot_segments()
    uri3 = URINorm('https://www.test.com/a/b/c/./../../g').remove_dot_segments()
    uri_removed_dot1 = 'https://www.test.com/a/c/d.html'
    uri_removed_dot2 = 'http://google.com/mid/6'
    uri_removed_dot3 = 'https://www.test.com/a/g'
    self.assertEqual(uri1, uri_removed_dot1)
    self.assertEqual(uri2, uri_removed_dot2)
    self.assertEqual(uri3, uri_removed_dot3)

  def test_remove_prefix(self):
    uri1 = URINorm('http://test.com').remove_prefix()
    uri2 = URINorm('https://test.com').remove_prefix()
    uri3 = URINorm('test.com').remove_prefix()
    uri_removed_prefix = 'test.com'
    self.assertEqual(uri1, uri_removed_prefix)
    self.assertEqual(uri2, uri_removed_prefix)
    self.assertEqual(uri3, uri_removed_prefix)
    

if __name__ == '__main__':
  unittest.main()