from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import App, Run
from .serializers import AppCreateSerializer, AppUpdateSerializer, RunSerializer
from rest_framework.decorators import action
from django.http import Http404
import subprocess
import docker


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AppCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return AppUpdateSerializer
        return AppCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class RunViewSet(viewsets.ModelViewSet):
    serializer_class = RunSerializer

    def get_queryset(self):
        app_id = self.kwargs.get('app_id')
        try:
            app = App.objects.get(id=app_id)
        except App.DoesNotExist:
            raise Http404("App does not exist")

        return Run.objects.filter(app=app)

    def create(self, request, app_id=None):
        if not App.objects.filter(id=app_id).exists():
            return Response({'message': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

        app = App.objects.filter(id=app_id).first()
        app_data = {
            'name': app.name,
            'image': app.image,
            'envs': app.envs,
            'command': app.command,
        }
        run = Run.objects.create(
            app=app, parameters=app_data, status="Running")

        docker_client = docker.from_env()

        # Create a Docker container based on app configuration
        container = docker_client.containers.run(
            image=app.image,
            command=app.command,
            environment=app.envs,
            labels={'l1': 'v1'},
            detach=True  # Run in the background
        )

        # Update run status based on container execution result
        try:
            # Adjust timeout as needed
            container.wait(timeout=app.execution_timeout)
            run.status = "Finished"
            run.save()
            return Response({'message': 'Container started and finished successfully.'}, status=status.HTTP_200_OK)
        except docker.errors.ContainerError as e:
            error_message = str(e)
            run.status = "Finished"
            run.save()
            return Response({'message': f'Error starting container: {error_message}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            run.status = "Finished"
            run.save()
            return Response({'message': f'Error starting container: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
