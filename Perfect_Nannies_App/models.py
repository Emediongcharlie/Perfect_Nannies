from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('guardian', 'guardian'),
        ('nanny', 'nanny'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.get_full_name()


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    name_of_next_of_kin = models.CharField(max_length=100)
    phone_number_of_next_of_kin = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.user.get_full_name()


class Nanny(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="nanny")
    phone_number = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    name_of_next_of_kin = models.CharField(max_length=100)
    phone_number_of_next_of_kin = models.CharField(max_length=11, unique=True)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, null=True, blank=True, related_name='nannies')

    guarantor = models.TextField()

    def __str__(self):
        return self.user.get_full_name()
