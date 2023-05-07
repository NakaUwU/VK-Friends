from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=32)


class Requests(models.Model):
    req = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='requests')


class Friends(models.Model):
    friend = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='friends')
