from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# haga sus visatas aca

urlpatterns = [
    path('', views.home, name = 'home'),
    path('servicios', views.servicios, name = 'servicios'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('horas/pedir', views.pedir_hora, name = 'crear'), 
]
