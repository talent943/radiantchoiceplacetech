from django.urls import include, re_path as url
from rest_auth.views import PasswordResetConfirmView
from . import views
from .import HodViews, StaffViews, StudentViews
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
    url("home/", views.home, name="home"),
    # url('^signup/', SignUpView.as_view(), name='signup'),
    url('register/', views.register_user, name='register'),
    url('^signup/', views.signup, name='signup'),
    # url('register', views.register, name='register'),
    url('^login/', views.custom_login, name='login'),
    url('^logout/', views.custom_logout, name='logout'),
    # url('profile/<username>', views.profile, name='profile'),
    url('^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url('^profile/', views.profile, name='profile'),
    url('contact', views.contact, name="contact"),
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

    # URLS for Courses
    url('icdl-workforce/', views.icdl_workforce, name="icdl_workforce"),
    url('icdl-professional/', views.icdl_professional, name="icdl_professional"),
    url('icdl-digital-citizen/', views.icdl_digital_citizen, name="icdl_digital_citizen"),
    url('icdl-student/', views.icdl_student, name="icdl_student"),

    # Urls for Student
    url('student/', views.student, name="student"),
    url('contact/', views.contact, name="contact"),
    url('course/', views.course, name="course"),
    url('about/', views.about, name="about"),

]

    # url('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    # url('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    # url('student_apply_leave/', StudentViews.student_apply_leave, name="student_apply_leave"),
    # path('student_apply_leave_save/', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    # path('student_feedback/', StudentViews.student_feedback, name="student_feedback"),
    # path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
    # path('student_profile/', StudentViews.student_profile, name="student_profile"),
    # path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    # path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),