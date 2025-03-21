from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Adicione campos extras se necessário, por exemplo:
    # telefone = models.CharField(max_length=15, blank=True, null=True)
    pass

    def __str__(self):
        return self.username

