from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)


class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='clients_avatar', blank=True)
    telephone = models.ForeignKey(PhoneNumbers, on_delete=models.SET_NULL, null=True)
    client_location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.last_name
