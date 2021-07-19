import pdb

from django.contrib.auth.models import AbstractUser


# Create your models here.

class PyPlayyUser(AbstractUser):
    pass

    def is_buyer(self):
        return self.groups.filter(name='Buyer').exists()

    def is_provider(self):
        return self.groups.filter(name='Provider').exists()

    def __str__(self):
        return self.username
