from django.urls import path

from . import views


urlpatterns = [
    path('status', views.bank_status, name='status'),
    path('withdraw', views.bank_withdraw, name='withdraw'),
    path('set', views.bank_set, name='set'),
    path('_reset', views.bank_reset, name='reset'),
]
