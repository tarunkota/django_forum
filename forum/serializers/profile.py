from ..models import Profile
from rest_framework import serializers
from .badge import BadgeSerializer

class ProfileSerializer1(serializers.ModelSerializer):
    badges = BadgeSerializer(read_only=True,many=True)
    class Meta:
        lookup_field = 'username'
        model = Profile
        fields = ['username','firstname','lastname','dp','bio','followers','member_since','badges']