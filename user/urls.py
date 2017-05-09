from django.conf.urls import url
from . import views
app_name = 'user'
urlpatterns = [
    url(r'^$', views.profile_view, name = 'profile'),
    url(r'^register/$', views.register_view, name = 'register'),
    url(r'^register/(?P<slug>[\w-]+)/$', views.register_view, name = 'register_branch'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^login/(?P<slug>[\w-]+)/$', views.login_view, name = 'login_branch'),
    url(r'^home/$', views.home_view, name = 'home'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^details/(?P<slug>[\w-]+)/$', views.details_view, name = 'details'),
    url(r'^profile/$', views.profile_view, name = 'profile'),
    url(r'^artisans/(?P<query_type>[\w-]+)/$', views.artisans_view, name = 'artisans'),
    url(r'^artisans/$', views.artisans_view, name = 'artisans'),
]
