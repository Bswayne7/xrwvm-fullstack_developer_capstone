from django.contrib import admin
from .models import CarMake, CarModel

# Register models so they appear in Django Admin
admin.site.register(CarMake)
admin.site.register(CarModel)
