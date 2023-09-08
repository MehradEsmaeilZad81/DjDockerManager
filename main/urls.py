from django.urls import path, include
from .views import AppsAPIView

urlpatterns = [
    path('apps/', AppsAPIView.as_view(), name='app-list'),
    path('apps/<int:pk>/', AppsAPIView.as_view(), name='app-detail')
]
