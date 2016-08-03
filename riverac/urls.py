
from django.conf.urls import url,include
from django.conf.urls import url
from django.contrib import admin

import riverac.core.views

urlpatterns = [
	url(r'^noticia/(?P<slug>[\w_-]+)/$',riverac.core.views.noticia,name="noticia"),

	url(r'^$',riverac.core.views.home,name="home"),
    url(r'^admin/', admin.site.urls),
	
	url(r'^s3direct/', include('s3direct.urls')),

	url(r'^$',riverac.core.views.home,name="home"),
    url(r'^admin/', admin.site.urls),
]
