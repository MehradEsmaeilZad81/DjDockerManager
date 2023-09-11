from django.urls import path, include
from .views import AppsAPIView, RunsAPIView

urlpatterns = [
    path('apps/', AppsAPIView.as_view(), name='app-list'),
    path('apps/<int:pk>/', AppsAPIView.as_view(), name='app-detail'),
    path('apps/<int:pk>/run/', RunsAPIView.as_view()),
]
