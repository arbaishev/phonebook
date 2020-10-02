from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


phone_regex = RegexValidator(regex=r'^((\+\d)+([0-9]){7,15})$',
                             message='Phone number must be the following format: "+99999999"')


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField('Name', max_length=64, blank=False)
    surname = models.CharField('Surname', max_length=64, blank=False)
    patronymic = models.CharField('Patronymic', max_length=64, blank=False)
    phone_number = models.CharField('Phone number', max_length=64, validators=[phone_regex], blank=False)
    email = models.EmailField('E-mail', blank=True)
    address = models.TextField('Address', blank=True)
    comment = models.TextField('Comment', blank=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"
