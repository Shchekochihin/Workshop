from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    phone_number = models.CharField(max_length=20)


class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="clients_avatar")
    telephone = models.ForeignKey(PhoneNumbers, on_delete=models.SET_NULL, null=True)
    client_location = models.CharField(max_length=100)
    description = models.TextField
