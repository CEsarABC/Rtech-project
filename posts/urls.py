from django.conf.urls import url, include
from posts.views import project_page, project_create, edit_project, delete_post
from accounts import url_reset
from posts import views

urlpatterns = [
    url(r'^$', project_page, name="project_page"),
    url(r'^create/$', project_create, name="project_create"),
    url(r'^(?P<pk>\d+)/edit/$', edit_project, name='edit_project'),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post'),
    url(r'^createService/$',views.ServiceCreateView.as_view(),name='createService'),
]
