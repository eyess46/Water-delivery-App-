from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inner_page', views.inner_page, name='inner_page'),
    path('order_create', views.order_create, name='order_create'),
    path('home_cleaning', views.home_cleaning, name='home_cleaning'),
    path('order_success', views.order_success, name='order_success'),
    path('about', views.about, name='about'),
    path('cleaning_success', views.cleaning_success, name='cleaning_success'),

  
   
]











