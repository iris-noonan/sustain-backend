from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Badge
from .serializers.common import BadgeSerializer
from .serializers.populated import PopulatedBadgeSerializer

# Create your views here.
class BadgeListView(ListCreateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # this class gives read access to unauthenticated users, but restricts POST, PUT, PATCH & DELETE requests to authenticated users only

class BadgeDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Badge.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedBadgeSerializer
        else:
            return BadgeSerializer