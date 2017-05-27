from django.conf.urls import url
from . import views
# note that you can write '.' if importing a module from the current app


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
]