from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    materials_provided = models.CharField(max_length=100)

    def __str__(self):
        return self.name








