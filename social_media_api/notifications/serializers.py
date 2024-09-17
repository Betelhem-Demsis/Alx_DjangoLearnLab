from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class NotificationSerializer(serializers.ModelSerializer):
    actor = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'unread']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['target'] = str(instance.target)
        return representation