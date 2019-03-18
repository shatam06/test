from django.shortcuts import render,HttpResponse
from rest_framework import viewsets

from .models import data
from .serializers import dataSerializer




class dataView(viewsets.ModelViewSet):

    queryset=data.objects.all()
    serializer_class=dataSerializer

#def home(request):
   # return HttpResponse("ok", content_type='application/json')