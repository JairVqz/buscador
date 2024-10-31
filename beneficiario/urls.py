from django.urls import path
from beneficiario import views
from django.contrib import admin
from .views import ReportebenExcel

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.lista_beneficiarios, name='lista_beneficiarios'),
    path('beneficiarios/', views.beneficiariosApi),
    path('agregar_beneficiario/', views.agregar_beneficiario, name='agregar_beneficiario'),
    path('eliminar_beneficiario/<int:id>/', views.eliminar_beneficiario, name='eliminar_beneficiario'),
    path('editar_beneficiario/<int:id>/', views.editar_beneficiario, name='editar_beneficiario'),
    path('reporte_excel_padron/', ReportebenExcel.as_view(), name="reporte_excel_padron"),
]