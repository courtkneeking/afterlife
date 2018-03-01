from __future__ import unicode_literals
from django.db import models


class Subject(models.Model):
	subject_name = models.CharField(max_length = 100)
	birthday = models.CharField(max_length = 100)
	death_date = models.CharField(max_length = 100)
	profile_image = models.CharField(max_length = 300)
	slideshow = models.CharField(max_length = 300)
	gofundme = models.CharField(max_length = 300, null = True)

class Story(models.Model):
	story = models.CharField(max_length = 100, null = True)
	author = models.CharField(max_length = 500, null = True)
	subject = models.ForeignKey(Subject, related_name = "stories", null = True)

class Condolence(models.Model):
	condolence = models.CharField(max_length = 500, null = True)
	author = models.CharField(max_length = 500, null = True)
	subject = models.ForeignKey(Subject, related_name = "condolences", null = True)

class Friend(models.Model):
	name = models.CharField(max_length = 500, null = True)
	email = models.CharField(max_length = 100, null = True)
	subject = models.ForeignKey(Subject, related_name = "friends", null = True)

class Image(models.Model):
	image = models.CharField(max_length = 300)
	subject = models.ForeignKey(Subject, related_name = "images", null = True)

class Obituary(models.Model):
	obituary_image = models.CharField(max_length = 300, null = True)
	subject_description = models.CharField(max_length = 1000, null = True)
	subject_family = models.CharField(max_length = 1000, null = True)
	funeral_information = models.CharField(max_length = 1000, null = True)
	subject = models.ForeignKey(Subject, related_name = "obituaries", null = True)




