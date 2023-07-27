from django.urls import include, re_path as url
from . import views

app_name = 'users'

urlpatterns = [
    url('signup', views.signup, name='signup'),
    # url('register', views.register, name='register'),
    url('login', views.custom_login, name='login'),
    url('logout', views.custom_logout, name='logout'),
    # url('profile/<username>', views.profile, name='profile'),
    url('profile/(?P<username>\w+)/$', views.profile, name='profile'),
     url('profile/', views.profile, name='profile'),
    # url('activate/<uidb64>/<token>', views.activate, name='activate'),
    #url('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),
    #url('activate/<uidb64>/<token>', views.activate, name='activate'),

    # signed up
    # url('signup/', views.signup, name="signup"),  
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', views.activate, name='activate')
]