from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DocumentType)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Address)
