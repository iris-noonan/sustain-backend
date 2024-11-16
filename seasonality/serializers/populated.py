from products.serializers import ProductSerializer
from .common import SeasonSerializer

class PopulatedSeasonSerializer(SeasonSerializer):
    products = ProductSerializer(many=True)