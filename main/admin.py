from django.contrib import admin
from .models import Courses, Contact


class CoursesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "duration",
        "cost",
        "tutor"
    ]

class StudentAdmin(admin.ModelAdmin):
    fields = [
        "first_name",
        "last_name",
        "email_address",
        "date_enrolled",
        "course"
    ]


admin.site.register(Courses)
admin.site.register(Contact)
