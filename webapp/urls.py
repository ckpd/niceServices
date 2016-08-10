from django.conf.urls import include, url
from webapp import views
from webapp.views import CustomerOrderCreate, CustomerOrderUpdate, CustomerOrderDetailView, ThankYouPage, Carlist, CarDetailView, HomeTemplateView

#from webapp.views import vehicleToBeRentedCreateView, vehicleToBeRentedUpdateView, vehicleDetailView
#from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
#        url(r'^$', views.index, name='index'),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^create/$', CustomerOrderCreate.as_view(), name='CustomerOrder-add'),
    url(r'CustomerOrder/(?P<pk>[0-9]+)/$', CustomerOrderUpdate.as_view(), name='CustomerOrder-update'),
    url(r'^CustomerOrder/(?P<pk>[0-9]+)/$', CustomerOrderDetailView.as_view(), name='CustomerOrder-detail'),
    url(r'^thanks/$', ThankYouPage.as_view(), name='thanks'),
    url(r'^manage/$', views.Carlist, name='manage'),
    url(r'^details/(?P<pk>[-\w]+)/$', CarDetailView.as_view(), name='car-detail'),

]
