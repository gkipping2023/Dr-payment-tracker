from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:payment_id>/', views.delete_payment, name='delete_payment'),
]
