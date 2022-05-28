from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path('index/', views.index, name='index'),
    path('model/', views.model, name='model'),
    path('respuesta/<respuesta>/', views.respuesta, name='respuesta'),
    path('informe/', views.informe, name='informe'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)