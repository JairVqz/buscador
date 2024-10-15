from django.urls import path
from beneficiario import views
from django.contrib import admin

urlpatterns=[
    path('admin/', admin.site.urls),
    path('beneficiario/', views.beneficiariosApi),
    path('beneficiario/<int:id>/', views.beneficiariosApi, name='beneficiario-detail'),
    path('', views.lista_beneficiarios, name='lista_beneficiarios'),
    path('formulario/', views.formulario_beneficiario, name='formulario_beneficiario'),
    path('agregar_beneficiario/', views.agregar_beneficiario, name='agregar_beneficiario'),
    path('eliminar_beneficiario/<int:id>/', views.eliminar_beneficiario, name='eliminar_beneficiario'),
    path('editar_beneficiario/<int:id>/', views.editar_beneficiario, name='editar_beneficiario'),
]