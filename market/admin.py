from atexit import register
from django.contrib import admin
from market.models import Categories
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Categories, MPTTModelAdmin)
