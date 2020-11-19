from rest_framework import serializers
from .models import Vendedor, Productos

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id','nombre','agregado_por','fecha_creacion']

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model =Productos
        fields = ['id', 
        'proveedor', 
        'nomprod', 
        'precio', 
        'descrip',
        'agregado_por', 
        'fecha_creacion']
