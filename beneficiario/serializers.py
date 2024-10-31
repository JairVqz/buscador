from rest_framework import serializers
from beneficiario.models import Beneficiario, Area, Municipio

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ('id', 'folio_sd', 'nombres', 'apellido_paterno', 'apellido_materno', 'sexo', 'programa', 'area_programa', 'ejercicio', 'municipio')

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'prefijo', 'nombre_completo')

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        field = ('id', 'cve_mpio', 'cve_mpio_full', 'nombre', 'territorio')