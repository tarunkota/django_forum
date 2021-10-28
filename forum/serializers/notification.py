from ..models import Notification
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    actor = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ("notif_type","is_read","created","actor","post","id")


    def get_post(self,obj):
        return obj.Object.slug
    
    def get_actor(self,obj):
        return obj.Actor.username

    