from django.urls import path
from . import views

urlpatterns = [
    path('aurea/', views.francisco_view, name='aurea'),
]