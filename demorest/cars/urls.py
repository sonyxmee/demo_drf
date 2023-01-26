from django.urls import path
from .views import *

# app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view(), name='create_car'),
    path('list/', CarListView.as_view(), name='list_car'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='detail_car'),

]
