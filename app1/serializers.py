
from rest_framework import serializers
from .models import data

class dataSerializer(serializers.ModelSerializer):

    class Meta:
        model=data
        fields=('name','phone','address','birthday','general','password')
    

       

