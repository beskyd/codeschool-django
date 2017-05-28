from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_location/$', views.post_location, name = 'post_location'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += [
            url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
        ]
