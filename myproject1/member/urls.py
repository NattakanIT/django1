from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.members, name='member'),
]