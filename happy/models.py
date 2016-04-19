from django.db import models
from django.contrib.auth.models import User

class Point(models.Model):
    user = models.ForeignKey(User, related_name='points')
    level = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
