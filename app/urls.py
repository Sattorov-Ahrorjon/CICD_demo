from django.urls import path
from .views import main_page, index

urlpatterns = [
    path('', main_page, name='main'),
    path('about/', index, name='about')
]
