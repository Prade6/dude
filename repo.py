import urllib
import re

urls = ["https://simple.wikipedia.org/wiki/List_of_U.S._states", "http://galshir.com", "http://google.com", "http://youtube.com", "http://cnn.com", "http://nytimes.com", "http://crive.co"]

gettitle = '<title>(.+?)</title>'
pattern = re.compile(gettitle)

for i in urls:
	htmlfile = urllib.urlopen(i)
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print titles

