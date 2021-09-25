from django.db import models
from django.contrib.auth import get_user_model


class DocumentType(models.Model):
    value = models.CharField(max_length=10)
    description = models.CharField(max_length=30, null=True)
    enable = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.value}'

    # @property
    # def name(self) -> str:
    #     return f'{self.name}'
    #
    # @name.setter
    # def name(self, name: str):
    #     self.name = name
    #
    # @property
    # def enable(self) -> str:
    #     return f'{self.enable}'
    #
    # @enable.setter
    # def enable(self, enable: bool):
    #     self.enable = enable


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING)
    dni = models.CharField(max_length=11, unique=True)  # Document Number Identify
    email = models.EmailField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.dni}'  # Replace for user

    @property
    def full_name(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country}'


class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.state}'


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    alias = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=20)
    more_info = models.TextField(blank=True)
    guest = models.CharField(max_length=100, blank=True)
    mobile_guest = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.alias}, {self.city.name}, {self.profile.first_name}'
