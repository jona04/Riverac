from django.conf.urls import url
from django.contrib import admin

import riverac.core.views

urlpatterns = [
	url(r'^$',riverac.core.views.home,name="home"),
    url(r'^admin/', admin.site.urls),
]
