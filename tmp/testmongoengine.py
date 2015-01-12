from mongoengine import *
connect(
    'news',
    username='adminnews',
    password='news',
    host='127.0.0.1',
    port=27017
)


class tmpnews(Document):

	"""docstring for tmpnews"""

	category = StringField()
	comments = StringField()
	description = StringField()
	link = StringField()
	pubDate = StringField()
	title = StringField()

