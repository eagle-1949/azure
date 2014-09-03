from django.db import models

# Create your models here.

class Accounts(models.Model):
    account_name = models.CharField(max_length=40)
    account_key = models.CharField(max_length=60)
    def __unicode__(self):              # __str__ on Python 2
        return self.account_name
class Containers(models.Model):
    CONTAINER_ACCESS = (
        ('PR', 'Private'),
        ('PC', 'Public Container'),
        ('PB', 'Public Blob'),
    )
    account = models.ForeignKey(Accounts)
    container_name = models.CharField(max_length=40)
    container_access=models.CharField(max_length=2, choices=CONTAINER_ACCESS)
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField('email')
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    create_date = models.DateTimeField('create date')
class ContainerUser(models.Model):
    container = models.ForeignKey(Containers)
    user = models.ForeignKey(Users)
    create_date = models.DateTimeField('create date')


