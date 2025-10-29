from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
