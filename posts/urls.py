from django.conf.urls import url, include
from posts.views import project_create
from accounts import url_reset

urlpatterns = [
    url(r'^$', project_create, name="project_create"),
]