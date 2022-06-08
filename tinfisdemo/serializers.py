from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


        
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model =Women
        fields =('title','content','cat','is_published')
    
        
    