#Importaciones para autenticar
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Serializers y modelos
from .serializers import ProductosSerializer
from .models import Productos, Vendedor
from rest_framework import status

#Json
import json

#Errores
from django.core.exceptions import ObjectDoesNotExist

#Mensaje de Bienvenida
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome (request):
    content = {"mensaje": "Bienvenido a la tienda"}
    return JsonResponse(content)

# LISTAR
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def listar_prods(request):
    user = request.user.id 
    prods = Productos.objects.filter(agregado_por=user)
    serializer = ProductosSerializer(prods, many=True)
    return JsonResponse({'productos': serializer.data}, safe=False, status=status.HTTP_200_OK)

#CREAR
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def agregar_prod(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        vendedor = Vendedor.objects.get(id=payload["vendedor"])
        prod = Productos.objects.create(
            nomprod=payload["Nombre del Producto"],
            precio=payload["Precio"],
            agregado_por=user,
            vendedor=vendedor
        )
        serializer = ProductosSerializer(prod)
        return JsonResponse({'productos': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo salio muy mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#UPDATE
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def act_prod(request, prod_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        prod_item = Book.objects.filter(agregado_por=user, id=prod_id)
        prod_item.update(**payload)
        prod = Productos.objects.get(id=prod_id)
        serializer = ProductosSerializer(prod)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo salio muy mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#ELIMINAR
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def elim_prod(request, prod_id):
    user = request.user.id
    try:
        prod = Productos.objects.get(agregado_por=user, id=prod_id)
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo salio mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)