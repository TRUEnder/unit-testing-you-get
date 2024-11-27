import unittest
from you_get.common import *


class URLtoModuleDriver(unittest.TestCase):

    def test_valid_url(self):
        url = "https://www.youtube.com/watch?v=example_video"

        try:
            module, processed_url = url_to_module(url)
            print(f"Result -> Module: {module}, URL: {processed_url}")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")


    def test_unsupported_url(self):
        with self.assertRaises():
            url = "https://unsupported-website.com/video"


    def test_redirect_url(self):
        with self.assertRaises():
            url = "https://redirect.com/video"


if __name__ == '__main__' :
    unittest.main()