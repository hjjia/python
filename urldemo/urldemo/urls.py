"""urldemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appcalc import views as appcalc_views

urlpatterns = [
	# url(r'^$', appcalc_views.index, name='home'),
	url(r'add/(\d+)/(\d+)/$', appcalc_views.old_add2_redirect),
	url(r'new_add/(\d+)/(\d+)/$', appcalc_views.add1, name='add1'),
	# url(r'^add/$', appcalc_views.add, name='add'),
    url(r'^admin/', admin.site.urls),
]

