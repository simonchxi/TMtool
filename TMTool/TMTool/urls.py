"""TMTool URL Configuration

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

from django.conf.urls import *
from . import view, testdb, search
from django.contrib import admin
 
urlpatterns = [
    url(r'^$', view.base),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^testdbdel$', testdb.testdbdel),
    url(r'^testdbupdt$', testdb.testdbupdt),
 	url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search.search_post),
    url(r'^admin/', include(admin.site.urls)),
]
