from django.contrib import admin

# Register your models here.

from task.models import Client
from task.models import Manufacturer

admin.site.register(Client)
admin.site.register(Manufacturer)
