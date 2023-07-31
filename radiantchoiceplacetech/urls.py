"""
URL configuration for radiantchoiceplacetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path as url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from main.views import contact, success, about, home, course
from main import views
from users import views
from django_email_verification import urls as email_urls


admin.site.site_header = "RADIANT CHOICE PLACETECH Admin"
admin.site.site_title = "RADIANT CHOICE PLACETECH Admin"
admin.site.index_title = "Welcome to RADIANT CHOICE PLACETECH"

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url("^users/", include('users.urls')),
    url("^", include('main.urls')),
    url(r'', include('django.contrib.auth.urls')),
    url('email/', include(email_urls), name='email-verification'),
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    # url("student/", views.student, name="student"),
    # url("^contact/", views.contact, name="contact"),
    # url("^about/", views.about, name="about"),
    # url("^course/", views.course, name="course"),
    # url('', include('django.contrib.auth.urls'))
    # url(r'password_change/$',auth_views.PasswordChangeView.as_view(template_name='password_change.html',success_url='/accounts/password_change_done')),
    # url(r'password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')),
    # url(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html',subject_template_name='password_reset_subject.txt',success_url='/accounts/password_reset_done/',from_email='support@yoursite.ma')),
    # url(r'password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html')),
    # url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',success_url='/accounts/password_reset_complete/')),
    # url(r'password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)