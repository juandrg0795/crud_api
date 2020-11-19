from django.contrib import admin
from .models import Vendedor, Productos

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Productos)