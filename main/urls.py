from django.urls import include, re_path as url
from main import views

app_name = "main"

urlpatterns = [
    url("", views.home, name="home"),
    url("home", views.home, name="home"),
    url("student/", views.student, name="student"),
    url("contact/", views.contact, name="contact"),
    url("about/", views.about, name="about"),
    url('course/', views.course, name="course"),
]