from django.contrib import admin

# Register your models here.
from tinfisdemo import *
from tinfisdemo.models import Category, Women

admin.site.register(Women)
admin.site.register(Category)