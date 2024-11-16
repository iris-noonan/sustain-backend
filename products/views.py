from rest_framework.views import APIView # class that creates our view
from rest_framework.response import Response # Send a HTTP response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer, PopulatedProductSerializer
from utils.exceptions import handle_exceptions
from utils.permissions import IsOwnerOrReadOnly

# Model
from .models import Product

# Create your views here.
class ListCreateProductView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Index Controller
    # Route: GET /products/
    @handle_exceptions
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # Create Controller
    # Route: POST /products/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        new_product = ProductSerializer(data=request.data)
        new_product.is_valid(raise_exception=True)
        new_product.save()
        return Response(new_product.data, status.HTTP_201_CREATED)
    

class RetrieveUpdateDestroyProductView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    # Show Controller
    # Route: GET /products/:pk/
    @handle_exceptions
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = PopulatedProductSerializer(product)
        return Response(serializer.data)

    # Delete Controller
    # Route: DELETE /products/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)

        self.check_object_permissions(request, product)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # Update Controller
    # Route: PUT /products/:pk/
    @handle_exceptions
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)

        self.check_object_permissions(request, product)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)