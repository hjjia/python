# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def old_add2_redirect(req, a, b):
	return HttpResponseRedirect(
		reverse('add1', args=(a, b))
	)


def add(req):
	a = req.GET['a']
	b = req.GET['b']
	c = int(a) + int(b)

	return HttpResponse(str(c))

def add1(req, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def index(req):
	return render(req, 'home.html')


