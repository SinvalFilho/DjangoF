from django.db import models

class UserProfile(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.cpf
