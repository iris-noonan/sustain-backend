from django.urls import path
from .views import SeasonListView, SeasonDetailView

urlpatterns = [
    path('', SeasonListView.as_view()),
    path('<int:pk>/', SeasonDetailView.as_view())
]