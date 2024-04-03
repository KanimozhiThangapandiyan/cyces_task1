from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from country.models import Country,State,City
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

class add_country(CreateView):
    model=Country
    fields=['countryname']
    template_name='country_create.html'
    success_url = reverse_lazy('home')
class countries(ListView):
    template_name='home.html'
    model=Country
    def get_queryset(self):
        qs=Country.objects.all()
        return qs
class update_country(UpdateView):
    model=Country
    fields=['countryname']
    template_name='country_update.html'
    success_url = reverse_lazy('home')
class delete_country(DeleteView):
    model=Country
    template_name='country_cnfm.html'
    success_url = reverse_lazy('home')


class add_state(CreateView):
    model=State
    fields=['state_name','country']
    template_name='state_create.html'
    success_url = reverse_lazy('states_list')
class states(ListView):
    template_name='states_list.html'
    model=State
    def get_queryset(self):
        qss =State.objects.all()
        return qss
class update_state(UpdateView):
    model=State
    fields=['state_name']
    template_name='state_update.html'
    success_url = reverse_lazy('states_list')
class delete_state(DeleteView):
    model=State
    template_name='state_cnfm.html'
    success_url = reverse_lazy('states_list')


class add_city(CreateView):
    model=City
    fields=['city_name','state','country']
    template_name='city_create.html'
    success_url = reverse_lazy('city_list')
class cities(ListView):
    template_name='city_list.html'
    model=City
    def get_queryset(self):
        qsc=City.objects.all()
        return qsc
class update_city(UpdateView):
    model=City
    fields=['city_name']
    template_name='city_update.html'
    success_url = reverse_lazy('city_list')
class delete_city(DeleteView):
    model=City
    template_name='city_cnfm.html'
    success_url = reverse_lazy('city_list')