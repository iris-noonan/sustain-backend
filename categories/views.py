from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Category
from .serializers.common import CategorySerializer
from .serializers.populated import PopulatedCategorySerializer

# Create your views here.
class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # this class gives read access to unauthenticated users, but restricts POST, PUT, PATCH & DELETE requests to authenticated users only

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedCategorySerializer
        else:
            return CategorySerializer