from django.urls import path
from . import views

urlpatterns = [
    path('order_overview/', views.orders_overview, name='order_overview'),
    path('new_order/', views.new_order, name='new_order'),
]