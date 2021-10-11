from ..models import Profile
from rest_framework import serializers
from .badge import BadgeSerializer
from .avatar import AvatarSerializer

class ProfileSerializer1(serializers.ModelSerializer):
    badges = BadgeSerializer(read_only=True,many=True)
    avatar = AvatarSerializer(read_only=True,many=False)

    class Meta:
        lookup_field = 'username'
        model = Profile
        fields = ['avatar','username','firstname','lastname','dp','bio','followers','member_since','badges']