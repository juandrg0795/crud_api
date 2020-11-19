from django.urls import include, path

from . import views

urlpatterns = [
    path('welcome',views.welcome),
    path('listar', views.listar_prods),
    path('agregar', views.agregar_prod),
    path('actualizar/<int:prod_id>', views.act_prod),
    path('eliminar/<int:prod_id>', views.elim_prod)
]