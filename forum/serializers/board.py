from ..models import Board,Profile
from rest_framework import serializers
from .profile import ProfileSerializer1

class BoardSerializer(serializers.ModelSerializer):
    admins = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ["id","title","slug","description","admins","created","updated","subscriberCount","icon"]
        lookup_field="slug"

    def get_admins(self,obj):
        return ProfileSerializer1(obj.admins.all(),many=True,read_only=True).data
