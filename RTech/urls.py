"""RTech URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index,testpage,about,contact,services
from accounts import urls as urls_accounts
from posts import urls as urls_posts

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^test/$', testpage, name='testpage'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^services/$', services, name='services'),
    url(r'^posts/', include(urls_posts)),
]
