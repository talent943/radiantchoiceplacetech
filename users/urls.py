from django.urls import include, re_path as url
from rest_auth.views import PasswordResetConfirmView
from . import views
# from users.views import SignUpView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'

urlpatterns = [
    #url("", views., name="home"),
    # url('^signup/', SignUpView.as_view(), name='signup'),
    url('register/', views.register_user, name='register'),
    url('^signup/', views.signup, name='signup'),
    # url('register', views.register, name='register'),
    url('^login/', views.custom_login, name='login'),
    url('^logout/', views.custom_logout, name='logout'),
    # url('profile/<username>', views.profile, name='profile'),
    url('^profile/(?P<username>\w+)/$', views.profile, name='profile'),
     url('^profile/', views.profile, name='profile'),
    # url('activate/<uidb64>/<token>', views.activate, name='activate'),
    #url('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),
    #url('activate/<uidb64>/<token>', views.activate, name='activate'),

    # signed up
    # url('signup/', views.signup, name="signup"),  
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', views.activate, name='activate'),
    # url(r'', include('django.contrib.auth.urls')),
    url(r'^password-reset/$',
        PasswordResetView.as_view(template_name='users/password_reset.html',
         email_template_name = 'users/password_reset_email.html',
         success_url = reverse_lazy('users:password_reset_done'))  ,
         name='password_reset'),
    # url('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    url('password-reset-done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    url('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    url('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    url('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]