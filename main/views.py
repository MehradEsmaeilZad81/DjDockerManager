from django.shortcuts import render
from rest_framework.views import APIView
from .models import App
from .serializers import AppCreateSerializer, AppUpdateSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


class AppsAPIView(APIView):
    def get(self, request):
        apps = App.objects.all()
        serializer = AppCreateSerializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        if App.objects.filter(name=name).exists():
            return Response({'message': 'App already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        if not App.objects.filter(id=pk).exists():
            return Response({'message': 'App not found'}, status=status.HTTP_404_NOT_FOUND)
        app = App.objects.filter(id=pk).first()
        serializer = AppUpdateSerializer(app, data=request.data)
        serializer.is_valid(raise_exception=True)

        if 'name' in serializer.validated_data:
            updated_name = serializer.validated_data['name']
            if App.objects.exclude(pk=pk).filter(name=updated_name).exists():
                return Response({'message': 'App with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        if not App.objects.filter(id=pk).exists():
            return Response({'message': 'App not found'}, status=status.HTTP_404_NOT_FOUND)
        app = App.objects.filter(id=pk).first()
        app.delete()
        return Response({'message': 'App deleted'}, status=status.HTTP_204_NO_CONTENT)
