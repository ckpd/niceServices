from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView, View, TemplateView
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render, redirect, render_to_response 
from .forms import CustomerOrderCreateForm, CustomerOrderUpdateForm
from .models import CustomerOrder, VehicleOrder, Rented
from django.views.generic import View 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.shortcuts import render
#from .models import vehicleToBeRentedCreateView, vehicle 
#from .forms import vehicleToBeRentedCreateForm,vehicleToBeRentedUpdateForm, UserForm
#from django.contrib.auth.decorators import login_required

class HomeTemplateView(TemplateView):
    template_name = 'webapp/home.html'
    model = CustomerOrder
    def get_context_data(self, **kwargs):
        return dict(
            super(HomeTemplateView, self).get_context_data(**kwargs),
            vehicle_orders=VehicleOrder.objects.all()[0:3]
        )

class CustomerOrderCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/register/'
    redirect_field_name = 'redirect_to'
    template_name = 'webapp/index.html'
    model = CustomerOrder
    form_class = CustomerOrderCreateForm  

    def get_context_data(self, **kwargs):
        return dict(
            super(CustomerOrderCreate, self).get_context_data(**kwargs),
            vehicle_orders=VehicleOrder.objects.all()[0:3]
        )

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CustomerOrderCreate, self).form_valid(form)
    
    
class CustomerOrderUpdate(UpdateView):
    template_name = 'webapp/customerdetails.html'
    model = CustomerOrder
    form_class = CustomerOrderUpdateForm
    success_url = "/thanks/"

    
    
class CustomerOrderDetailView(DetailView):
    
    queryset = CustomerOrder.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(CustomerOrderDetailView, self).get_object()
        # Record the last accessed date
        object.save()
        # Return the object
        return object
    

    
class ThankYouPage(TemplateView):
    template_name = 'webapp/thanks.html'



#make this make accessible only to admin   
@login_required
def Carlist(request):
    notavailable = Rented.objects.filter(is_Available=False)
    available = Rented.objects.filter(is_Available=True)

    context = {
        'available': available,
        'notavailable': notavailable,
    }
    return render(request, 'webapp/car_list.html', context)
    
class CarDetailView(DetailView):
    template_name = 'webapp/car_details.html'
    model = VehicleOrder



#class vehicleToBeRentedCreateView(CreateView):
#    model = vehicleToBeRentedCreateView
#    fields = '__all__'
#    
#class vehicleToBeRentedUpdateView(UpdateView):
#    model = vehicleToBeRentedCreateView
#    form_class = vehicleToBeRentedCreateForm
#
#class vehicleDetailView(DetailView):
#    template_name = 'webapp/car_details.html'
#    model = vehicleToBeRentedCreateView
#

#    
#
#class UserForm(View):
#    form_class = UserForm
#    template_name = 'webapp/login.html'
#    
#    def get(self, request):
#        form = self.form_class(None)
#        return render(request, self.template_name, {'form':form})
#    
#    
#    def get(self, request):
#        form = self.form_class(request.POST)
#        
#        if form.is_valid():
#            user = form.save(commit=False)
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
#            user.save()
#
#
#

























#from django.views.generic import ListView, DetailView 
#from .models import IceCreamStore
#from django.http import HttpResponseRedirect, HttpResponse
#from django.shortcuts import render, redirect, render_to_response 
#from django.contrib.auth import authenticate, login
#from django.views.generic import FormView
#from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#
#from django import template
#from django.template.loader import get_template 
#from django import forms
#from django.template import Context
#
#def index(request):
#    if request.method == "POST":
#        form = CustomerOrderForm(request.POST)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                CustomerOrder.customer = request.user
#                return render(request, 'webapp/index.html', {'CustomerOrder': CustomerOrder})
#            else:
#                return render(request, 'music/login.html', {'error_message': 'Invalid login'})
#            return render(request, 'music/login.html')
#
##
##def index(request):
##    if request.method == "POST":
##        form = CustomerOrderForm(request.POST)
##        if form.is_valid():
##            CustomerOrder = form.save(commit=False)
##            print CustomerOrder
##            CustomerOrder.customer = request.user
##            form.save()webapp/registr
##            return redirect('/register/')
##        else:
##            variables = RequestContext(request, {'form': form})
##            return render_to_response('webapp/index.html', variables)
##    else:
##        form = CustomerOrderForm(initial={'user': request.user})
##    variables = RequestContext(request, {'form': form})
##    return render_to_response('webapp/index.html', variables)
#
#def UserFormView(request):
#    form = UserForm(request.POST or None)
#    if form.is_valid():
#        user = form.save(commit=False)
#        username = form.cleaned_data['username']
#        user.save()
#        CustomerOrder = form.save()
#
#        user = authenticate(username=username)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                albums = Album.objects.filter(user=request.user)
#                return render(request, 'music/index.html', {'albums': albums})
#    context = {
#        "form": form,
#    }
#    return render(request, 'webapp/registration_form.html', context)
