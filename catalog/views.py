from django.views.generic import ListView, View
from django.db.models import Q
from django.shortcuts import render

from catalog.forms import CarForm
from catalog.models import Car


class ListCar(ListView):
    model = Car
    template_name = 'cars_list.html'


class FilterListView(View):
    def post(self, request):
        params = request.POST
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
        return render(request, 'filter_list.html', context={'cars': Car.objects.filter(query)})


class CarSearchView(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'cars_form.html', context={'form': form})
