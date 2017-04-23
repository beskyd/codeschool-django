from django.conf.urls import url
from . import views
# note that you can write '.' if importing a module from the current app


urlpatterns = [
    url(r'^$', views.index),
]