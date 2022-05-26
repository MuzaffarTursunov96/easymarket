from django.forms import model_to_dict
from django.shortcuts import render
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import WomenSerializer
# Create your views here.



        
class WomenAPIView(APIView):
    def get(self, request):
        lst=Women.objects.all()
        sr=WomenSerializer(lst,many=True)
        return Response({'data':sr.data});
    
    def post(self, request):
        serializer=WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'title': serializer.data})
    
    def put(self, request, *args,**kwargs):
        print(kwargs)
        pk=kwargs.get('pk',None)
        
        if not pk :
            return Response({'error':'Something went wrong'})
        try:
            instance=Women.objects.get(pk)
        except:
            return Response({'error':'Object does not exists'})
        print(instance)
        serializer=WomenSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data})
    
# class WomenAPIView(generics.ListAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
