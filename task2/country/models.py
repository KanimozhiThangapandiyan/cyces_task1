from django.db import models

class Country(models.Model):
    uuid = models.UUIDField(default=models.UUIDField().auto_created, editable=False)
    countryname = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.countryname

class State(models.Model):
    uuid = models.UUIDField(default=models.UUIDField().auto_created, editable=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class City(models.Model):
    uuid = models.UUIDField(default=models.UUIDField().auto_created, editable=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

    
