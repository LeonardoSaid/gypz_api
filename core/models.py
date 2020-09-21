from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .validators import validate_cpf, validate_cpf_regex
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    cpf = models.CharField(max_length=40, validators=[
                           validate_cpf_regex, validate_cpf], unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.FloatField()
    birth_date = models.DateTimeField()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'salary', 'birth_date']

    objects = CustomUserManager()

    def __str__(self):
        return self.cpf