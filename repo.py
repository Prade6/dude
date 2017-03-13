import urllib
import re

urls = ["http://galshir.com", "http://google.com", "http://youtube.com", "http://cnn.com", "http://nytimes.com"]

gettitle = '<title>(.+?)</title>'
pattern = re.compile(gettitle)

for i in urls:
	htmlfile = urllib.urlopen(i)
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print titles