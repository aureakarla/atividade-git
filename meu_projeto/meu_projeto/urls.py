from django.urls import path
from . import views

urlpatterns = [
    path('aurea/', views.aurea_view, name='aurea'),
    path('thicy/', views.thicy_view, name='thicy'),
]                                                                   