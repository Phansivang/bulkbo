from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class sender_name(models.Model):
    sendername = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.sendername

class sender_number(models.Model):
    number_list = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.number_list


