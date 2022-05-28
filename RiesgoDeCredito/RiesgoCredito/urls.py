from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('model/', views.model, name='model'),
    path('respuesta/<respuesta>/', views.respuesta, name='respuesta'),
]