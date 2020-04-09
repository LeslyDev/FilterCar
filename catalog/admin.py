from django.contrib import admin
from catalog.models import Car

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass