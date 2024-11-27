import unittest
from you_get.common import *

import sys
from unittest import mock
import shutil

class YouGetUnitTest(unittest.TestCase):
    def match1_driver(self):
        text = 'https://docs.python.org/3/library/importlib.html'
        patterns = ['https?://[^/]+(?:/[^/]+)*', 'https?://[^/]+(/.*)']
        matching_str = match1(text)

        patterns = [
            'ftp://[^/]+(?:/[^/]+)*', # return None
            'https?://([^/]+)', # return domain
            ['https?://[^/]+(?:/[^/]+)*', 'https?://[^/]+(/.*)'], # return list of matching string
            ['https?://([^/]+)\.com', 'https?://[^/]+(/.*)\.php$'] # return empty list
        ]

        matching_str = match1(text, patterns[0])
        self.assertEqual(matching_str, None, "Return None case failed")

        matching_str = match1(text, patterns[1])
        self.assertEqual(matching_str, 'docs.python.org', "Return domain case failed")

        matching_str = match1(text, patterns[2])
        self.assertEquals(matching_str, [], "Return list of matching string case failed")

        matching_str = match1(text, patterns[3])
        self.assertEquals(matching_str, None, "Return empty list case failed")


    def launch_player_driver():
        test_cases = [
            ((3, 2), True, "Testing with Python < 3.3 and player available"),  # Simulate Python 3.2 and player available
            ((3, 2), False, "Testing with Python < 3.3 and player not available"),  # Simulate Python 3.2 and player not available
            ((3, 3), True, "Testing with Python >= 3.3 and player available"),  # Simulate Python 3.3 and player available
            ((3, 3), False, "Testing with Python >= 3.3 and player not available")  # Simulate Python 3.3 and player not available
        ]
        
        for version, player_available, description in test_cases:
            print(description)
            
            with mock.patch.object(sys, 'version_info', version):
                with mock.patch.object(shutil, 'which', return_value="player" if player_available else None):
                    launch_player(player="player", urls=["example.mp4"])



if __name__ == '__main__' :
    unittest.main()