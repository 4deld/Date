from django.contrib import admin

# Register your models here.
from .models import Person, Info

admin.site.register(Person)

admin.site.register(Info)