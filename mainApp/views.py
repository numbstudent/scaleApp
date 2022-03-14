from mainApp.forms import *
from mainApp.models import *
from django.shortcuts import get_list_or_404, render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError, Sum, Q, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django import template
from django.db import IntegrityError


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *

register = template.Library()

loginpage = 'login'

@login_required(login_url=loginpage)
def index(request):
    return render(request,'home.html')


@csrf_exempt
def ProductList(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ProductDetail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

@csrf_exempt
def RegisterList(request):
    if request.method == 'GET':
        register = Register.objects.all()
        serializer = RegisterSerializer(register, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        code = data['code']
        product = Product.objects.filter(code=code).values_list('id').last()[0]
        data['product'] = product
        data['status'] = 0
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            except IntegrityError:
                return JsonResponse({"error":"data sudah ada"}, status=400)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def RegisterFilteredList(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        code = data['code']
        register = Register.objects.filter(batchno=data['batchno'], product__code=code).values('product__name', 'batchno', 'boxno', 'status', 'id')
        serializer = RegisterSerializer(register, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def RegisterDetail(request, pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegisterSerializer(register)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(register, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        register.delete()
        return HttpResponse(status=204)