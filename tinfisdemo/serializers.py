from rest_framework import serializers
from .models import *




# class WomenModel:
#     def __init__(self,title,content):
#         self.title=title
#         self.content=content
        
class WomenSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    content= serializers.CharField()
    time_create =serializers.DateTimeField()
    time_update =serializers.DateTimeField()
    is_published =serializers.BooleanField(default=True)
    cat_id=serializers.IntegerField()
    
    def create(self,validated_data):
        return Women.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.time_update=validated_data.get('time_update',instance.time_update)
        instance.is_p
        
        pass
        
    