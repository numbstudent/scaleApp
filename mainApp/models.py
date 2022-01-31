from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class Batch(models.Model):
    no = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class Register(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    boxno = models.IntegerField()
    status = models.IntegerField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class Logging(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    weighing = models.FloatField()
    register = models.ForeignKey(Register, on_delete=models.CASCADE)