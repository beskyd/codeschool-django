from django.conf.urls import url
from . import views
# note that you can write '.' if importing a module from the current app
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += [
            url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
        ]