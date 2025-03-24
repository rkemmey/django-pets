from django.contrib import admin

# Register your models here.
from .models import Owner, Cat, Bird, Dog, Exotic_Animal

admin.site.register([Owner, Cat, Bird, Dog, Exotic_Animal])
