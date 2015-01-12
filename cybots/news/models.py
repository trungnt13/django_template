from django.db import models
from mongoengine import *
import datetime

# Create your models here.


class tmpnews(Document):

	"""New Feed model"""

	category = StringField()
	comments = StringField()
	description = StringField()
	link = StringField()
	pubDate = StringField()
	title = StringField()
