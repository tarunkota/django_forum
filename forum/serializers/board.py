from ..models import Board,Profile
from rest_framework import serializers
from .profile import ProfileSerializer1

class BoardSerializer(serializers.ModelSerializer):
    admins = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ["title","slug","description","cover","admins","created","updated","subscriberCount"]
        lookup_field="slug"

    def get_admins(self,obj):
        return ProfileSerializer1(Profile.objects.filter(user__in=obj.admins.all()),many=True,read_only=True).data
