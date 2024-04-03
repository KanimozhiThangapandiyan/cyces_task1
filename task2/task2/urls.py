"""
URL configuration for task2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from country.views import add_country,countries,update_country,delete_country,add_state,states,update_state,delete_state,cities,add_city,update_city,delete_city

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',countries.as_view(), name='home'),
    path('home/',add_country.as_view(),name='country_create'),
    path('country_update/<int:pk>/',update_country.as_view(), name='country_update'),
    path('country_cnfm/<int:pk>/',delete_country.as_view(), name='country_delete'),
    #path('',add_country.as_view()),
    #path('home/',countries.as_view(), name='home'),

    path('state/',states.as_view(), name='states_list'),
    path('state_list/',add_state.as_view(),name='state_create'),
    path('state_update/<int:pk>/',update_state.as_view(), name='state_update'),
    path('state_delete/<int:pk>/',delete_state.as_view(), name='state_delete'),

    path('city/',cities.as_view(), name='city_list'),
    path('city_list/',add_city.as_view(),name='city_create'),
    path('city_update/<int:pk>/',update_city.as_view(), name='city_update'),
    path('city_delete/<int:pk>/',delete_city.as_view(), name='city_delete'),


]
