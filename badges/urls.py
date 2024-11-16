from django.urls import path
from .views import BadgeListView, BadgeDetailView

urlpatterns = [
    path('', BadgeListView.as_view()),
    path('<int:pk>/', BadgeDetailView.as_view())
]