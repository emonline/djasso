"""djasso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myasso.views import adherents, associations

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adherents$', adherents),
    url(r'^associations/(\w*)/adherents$', adherents, name='association_adherents_list'),
    url(r'^associations/(\w*)$', associations, name='association_list'),
    url(r'^associations$', associations),
]
