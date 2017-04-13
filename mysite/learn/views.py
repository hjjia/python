# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(req):
	return HttpResponse(u'欢迎光临 Django')
