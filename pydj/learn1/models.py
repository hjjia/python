# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):
	name = models.CharField(max_length=50)
	qq = models.CharField(max_length=10)
	addr= models.TextField()
	email = models.EmailField()

	def __unicode__(self):
		return self.name



@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
	content = models.TextField()
	score = models.IntegerField()
	tags = models.ManyToManyField('Tag')

	def __unicode__(self):
		return self.title


@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
