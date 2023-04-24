from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Organisation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Permission(models.Model):
    user_email = models.EmailField(default=None)
    organisation_name = models.CharField(max_length=100,default=None)
    READ = 'READ'
    WRITE = 'WRITE'
    READANDWRITE = 'READANDWRITE'
    ADMIN = 'ADMIN'
    PERMISSION_CHOICES = [
        (READ, 'Read'),
        (WRITE, 'Write'),
        (READANDWRITE,'Read and Write'),
        (ADMIN, 'Admin'),
    ]
    access_level = models.CharField(
        max_length=20,
        choices=PERMISSION_CHOICES,
        default=READ,
    )

    def __str__(self):
        return f"{self.user_email} - {self.access_level} - {self.organisation}"