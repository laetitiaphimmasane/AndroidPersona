from django.db import models

class Persona (models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address_street = models.CharField(max_length=150)
    address_number = models.IntegerField()
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=70)
    postcode = models.IntegerField()
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    age = models.IntegerField()
    picture =  models.CharField(max_length=150)
    
    
    def __str__(self):
        return f"Persona ({id}) {self.first_name} {self.last_name}"
