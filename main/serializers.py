from rest_framework import serializers
from .models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

    def validate(self, data):
        if data['name'] == '' or data['image'] == '':
            raise serializers.ValidationError(
                'name, image fields are required')

        return data

    def validate_envs(self, value):
        if isinstance(value, dict):
            return value

        try:
            # Attempt to parse 'envs' as JSON
            parsed_data = json.loads(value)
            if not isinstance(parsed_data, dict):
                raise serializers.ValidationError(
                    "envs must be a JSON object (dictionary).")

        except JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON format for envs.")

        return parsed_data
