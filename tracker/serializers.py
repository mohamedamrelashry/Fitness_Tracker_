from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'distance', 'calories_burned', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('activity_type'):
            raise serializers.ValidationError({'activity_type': 'This field is required.'})
        if not data.get('duration_minutes') and data.get('duration_minutes') != 0:
            raise serializers.ValidationError({'duration_minutes': 'This field is required.'})
        if not data.get('date'):
            raise serializers.ValidationError({'date': 'This field is required.'})
        return data
