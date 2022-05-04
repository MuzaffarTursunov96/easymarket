from atexit import register
from django.contrib import admin
from market.models import Categories

# Register your models here.
admin.site.register(Categories)
