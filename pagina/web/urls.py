from django.urls import path
from web import views

urlpatterns = [
    path('agregar_aro/', views.agregar_aro, name='agregar aro'),
    path('agregar_cinto/', views.agregar_cinto, name='agregar cinto'),
    #path('malla_formulario/',views.malla_formulario, name='agregar malla')
    path('agregar_malla/', views.agregar_malla, name='agregar_malla'),
]