from you_get.common import *

text = 'https://docs.python.org/3/library/importlib.html'
patterns = ['https?://[^/]+(?:/[^/]+)*', 'https?://[^/]+(/.*)']
matching_str = match1(text, patterns)

print(matching_str)