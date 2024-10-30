from django.urls import path
from beneficiario import views
from django.contrib import admin

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.lista_beneficiarios, name='lista_beneficiarios'),
]