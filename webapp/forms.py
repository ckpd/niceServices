
from django.contrib.auth.models import User
#from .models import vehicleToBeRentedCreateView
from .models import CustomerOrder
from django import forms

class CustomerOrderCreateForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['Vehicle','Pick_Up', 'Drop_Off', 'Pick_Up_Date', 'Drop_Off_Date',  ]
        widgets = {
            'Vehicle': forms.Select(attrs={'default': 'City, AirPort, Address'}),
            'Pick_Up': forms.TextInput(attrs={'placeholder': 'City, AirPort, Address'}),
            'Drop_Off': forms.TextInput(attrs={'placeholder': 'City, AirPort, Address'}),
            'Pick_Up_Date': forms.TextInput(attrs={'placeholder': 'DD/MM/YYY'}),
            'Drop_Off_Date': forms.TextInput(attrs={'placeholder': 'DD/MM/YYY'}),
     
            '__all__': forms.TextInput(attrs={'class': 'input'}),
        }

class CustomerOrderUpdateForm(CustomerOrderCreateForm):
    class Meta(CustomerOrderCreateForm.Meta):
        # show all the fields!
        fields = '__all__'
        exclude = ['created_by']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', 'password']