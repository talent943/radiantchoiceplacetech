from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import os
from django.contrib.auth import get_user_model
from django.conf import settings

COURSE_CHOICES = (
    ("SELECT-COURSE", "SELECT COURSE"),
    ("ICDL-WORK-FORCE", "ICDL WORK FORCE"),
    ("ICDL-PROFESSIONAL", "ICDL PROFESSIONAL"),
    ("ICDL-STUDENT", "ICDL STUDENT"),
    ("ICDL-DIGITAL-CITIZEN", "ICDL DIGITAL CITIZEN"),
)

COURSE_COSTS = (
    ("one-thousand", "R1000.00"),
    ("two-thousand", "R2000.00"),
    ("three-thousand", "R3000.00"),
    ("four-thousand", "R4000.00"),
    ("five-thousand", "R5000.00"),
)

CONTACT_CHOICES = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)



class Courses(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=200, default="", blank=True)
    cost = models.CharField(max_length=30,
                  choices=COURSE_COSTS,
                  default="SELECT-COURSE-COST"
                )
    tutor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default='', blank=True)
    course = models.CharField(max_length=30,
                  choices=COURSE_CHOICES,
                  default="SELECT-COURSE"
                )
    email_address = models.TextField()
    phone_number = models.CharField(max_length=12)
    date_enrolled = models.DateTimeField('Date modified', default=timezone.now)
    courses = models.ForeignKey(Courses, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutor = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.email_address


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    mode_of_contact = models.CharField(
                            max_length=50,
                            choices = CONTACT_CHOICES,
                            default = 'email'
                            )
    course_categories = models.CharField(
                            max_length=50,
                            choices = COURSE_CHOICES,
                            default = 'SELECT-COURSE'
                            )
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email


class Tutor(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE,primary_key=True,related_name='Tutor')
    username = models.CharField(max_length=250)
    tutor_number = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

    def get_absolute_url(self):
        return reverse('classroom:tutor_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

