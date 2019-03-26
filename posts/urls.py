from django.conf.urls import url, include
from posts.views import project_page, project_create, edit_project
from accounts import url_reset

urlpatterns = [
    url(r'^$', project_page, name="project_page"),
    url(r'^create/$', project_create, name="project_create"),
    url(r'^(?P<pk>\d+)/edit/$', edit_project, name='edit_project')
]