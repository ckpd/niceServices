from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models



class VehicleOrder(models.Model):
    Make = models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Aircondition = models.CharField(max_length=200)
    Transmission = models.CharField(max_length=200, default='Automatic')
    logo = models.FileField(max_length=200)
    CostPerDay = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.Model + '-' + self.Make
    
    
    
class CustomerOrder(models.Model):
    Vehicle = models.ForeignKey(VehicleOrder)
    Pick_Up = models.CharField(max_length=200, default = "")
    Drop_Off = models.CharField(max_length=200, default = "")
    Pick_Up_Date = models.CharField(max_length=200, default = "")
    Drop_Off_Date = models.CharField(max_length=200, default = "")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,)
    First_Name = models.CharField(max_length=200, default = "")
    Last_Name = models.CharField(max_length=200, default = "")
    Telephone_Number = models.CharField(max_length=20, blank=True)
    Age = models.CharField(max_length=20, blank=True)
    Email_Address = models.CharField(max_length=50, blank=True)
    City = models.CharField(max_length=200, default = "")
    State = models.CharField(max_length=200, default = "")
    Country = models.CharField(max_length=200, default = "")
    Licence_Number = models.CharField(max_length=200, default = "")
    Expiration_Date = models.CharField(max_length=200, default = "")
    
    def __str__(self):
        return self.First_Name + ' - ' + self.Last_Name    
    
    def get_absolute_url(self):
        return reverse('webapp:CustomerOrder-update', kwargs={'pk': self.pk})
    
    
    
class Rented(models.Model):
    VehicleOrder = models.ForeignKey(VehicleOrder)
    CustomerOrder = models.ForeignKey(CustomerOrder)
    is_Available = models.BooleanField(default=True)

    def __str__(self):
        return self.VehicleOrder.Make