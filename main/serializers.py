from rest_framework import serializers
from .models import App
import json


class AppCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = App
        fields = ['id', 'name', 'image', 'envs', 'command']

    def validate(self, data):
        if data['name'] == '' or data['image'] == '':
            raise serializers.ValidationError(
                'name, image fields are required')

        return data

    def validate_envs(self, value):
        if isinstance(value, dict):
            return value
        else:
            raise serializers.ValidationError(
                "envs must be a JSON object (dictionary).")


class AppUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255, required=False)
    image = serializers.CharField(max_length=255, required=False)
    envs = serializers.JSONField(required=False)
    command = serializers.CharField(max_length=255, required=False)

    def update(self, instance, validated_data):
        # Update the fields specified in validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_envs(self, value):
        if isinstance(value, dict):
            return value
        else:
            raise serializers.ValidationError(
                "envs must be a JSON object (dictionary).")
