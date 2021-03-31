from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    passby = models.CharField(max_length=50, blank=True)

# for user signal token creation
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance = None, created=False, **kwargs):
#     Token.objects.create(user=instance)

# for relations in drf
class Singer(models.Model):
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete = models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    