from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, RunViewSet

router = DefaultRouter()
router.register(r'apps', AppViewSet)

# Define a nested router for runs under apps
runs_router = DefaultRouter()
runs_router.register(r'run', RunViewSet, basename='run')

urlpatterns = [
    path('', include(router.urls)),
    # Nested runs route under apps
    path('apps/<int:app_id>/', include(runs_router.urls)),
]
