from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    date_of_hire = models.DateField()
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.first_name

