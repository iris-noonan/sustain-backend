from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Season
from .serializers.common import SeasonSerializer
from .serializers.populated import PopulatedSeasonSerializer

# Create your views here.
class SeasonListView(ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # this class gives read access to unauthenticated users, but restricts POST, PUT, PATCH & DELETE requests to authenticated users only

class SeasonDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Season.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedSeasonSerializer
        else:
            return SeasonSerializer