from products.serializers import ProductSerializer
from .common import CategorySerializer

class PopulatedCategorySerializer(CategorySerializer):
    products = ProductSerializer(many=True)