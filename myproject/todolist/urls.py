from django.urls import path
from .views import base, about_us

urlpatterns = [
    path('', base, name='base'),
    path('about_us', about_us, name='about_us')
]