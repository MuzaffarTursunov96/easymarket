from django.forms import model_to_dict
from django.shortcuts import render
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404
from .serializers import WomenSerializer
from rest_framework import viewsets
# Create your views here.



        
class WomenAPIViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Women.objects.all()
        serializer = WomenSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Women.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = WomenSerializer(user)
        return Response(serializer.data)
    
    # def list(self, request):
    #     pass

    def create(self, request):
        pass

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):
        print(pk)
        queryset = Women.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = WomenSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    
    # def get(self, request):
    #     lst=Women.objects.all()
    #     sr=WomenSerializer(lst,many=True)
    #     return Response({'data':sr.data});
    
    # def post(self, request):
    #     serializer=WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'title': serializer.data})
    
    # def put(self, request, *args,**kwargs):
    #     pk=kwargs.get('pk',None)
    #     if not pk :
    #         return Response({'error':'Something went wrong'})
    #     try:
    #         instance=Women.objects.get(pk=pk)
    #     except:
    #         return Response({'error':'Object does not exists'})
    #     serializer=WomenSerializer(data=request.data,instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post':serializer.data})
    
    # def delete(self, request,*args,**kwargs):
    #     pk=kwargs.get('pk',None)
    #     if not pk:
    #         return Response({'error':'Something went wrong'})
    #     try:
    #         women=Women.objects.get(pk=pk)
    #     except:
    #         return Response({'error':'Object not found'})
        
    #     women.delete()
    #     return Response({'success':'Women deleted successfully!'})    
    
# class WomenAPIView(generics.ListAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
