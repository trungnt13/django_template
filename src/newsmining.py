from lxml import objectify as XML
from lxml import html as HTML
import re
import urllib2
import cgi

#########################################################
# Mining
#########################################################
rssURL = {
    'http://www.reuters.com/tools/rss': ('//*[@class="xmlLink"]/a', '//*[@class="xmlLink"]/a'),
}


def miningRSSLink(url, pathToTitle, pathToLink):
	html = HTML.parse(urllib2.urlopen(url))
	root = html.getroot()
	titles = root.xpath(pathToTitle)
	links = root.xpath(pathToLink)

	from itertools import izip
	rss = {t.text_content(): l.get('href') for t, l in izip(titles, links)}
	return rss


rss = []
for url, path in rssURL.iteritems():
	rss.append(miningRSSLink(url, path[0], path[1]))

news = []
tags = ['category', 'comments', 'description', 'link', 'pubDate', 'title']
for feed in rss:
	for title, url in feed.iteritems():
		print("Parsing %s:" % title)
		try:
			xml = XML.parse(urllib2.urlopen(url))
			root = xml.getroot()
			items = xml.xpath('//item')
			for i in items: # parsing each new
				tmp = {}
				for tag in tags:
					elements = [repr(x) for x in i.xpath('.//' + tag)]
					tmp[tag] = ','.join(elements)[1:-1]
				news.append(tmp)
		except Exception as exp:
			print("Error parsing: %s" % exp)
#########################################################
# Save to database
#########################################################
# import pymongo as mongo

# conn = mongo.MongoClient()
# db = conn['news']
# coll = db['tmpnews']

# for new in news:
# 	coll.update(
#             {
#                 'title': new['title'],
#                 'link': new['link']
#             }, new, upsert=True)
