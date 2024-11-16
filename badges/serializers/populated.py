from products.serializers import ProductSerializer
from .common import BadgeSerializer

class PopulatedBadgeSerializer(BadgeSerializer):
    products = ProductSerializer(many=True)