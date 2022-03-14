from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code','createdon','updatedon']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'product', 'batchno','boxno','status','createdon','updatedon']

class RegisterFilteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'product', 'batchno','boxno','status','createdon','updatedon']