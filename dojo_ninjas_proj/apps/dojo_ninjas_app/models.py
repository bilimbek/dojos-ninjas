from django.db import models

# Create your models here.
class Dojos (models.Model):
    name = models.CharField(max_length=45)
    city = models.TextField(max_length=45)
    state = models.TextField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ninjas (models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojos= models.ForeignKey(Dojos,related_name="ninjas", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

