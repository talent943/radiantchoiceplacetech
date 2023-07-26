from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    STATUS = (
        ('student', 'student'),
        ('tutor', 'tutor'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='student')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='image/user.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username
