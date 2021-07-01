from django.contrib.auth.models import AbstractUser


# Create your models here.

class PyPlayyUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
