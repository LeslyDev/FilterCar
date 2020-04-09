from django.urls import path

from catalog.views import ListCar, CarSearchView, FilterListView

urlpatterns = [
    path('list/', ListCar.as_view(), name='list_url'),
    path('search/', CarSearchView.as_view(), name='m'),
    path('filter_list/', FilterListView.as_view(), name='main')
]