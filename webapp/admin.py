from django.contrib import admin
#from .models import vehicle, vehicleToBeRentedCreateView
from .models import CustomerOrder, VehicleOrder, Rented
#
admin.site.register(VehicleOrder)
admin.site.register(CustomerOrder)
admin.site.register(Rented)
