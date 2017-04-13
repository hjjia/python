# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(req):
	return render(req, 'learn/home.html')
