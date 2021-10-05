from ..models import Post
from rest_framework import serializers
from .profile import ProfileSerializer1

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["title","slug","owner","board","text","photo","video","score","active","created","updated","efficientMode","upvotes_count","downvotes_count","comments_count"]
        lookup_field = 'slug'


    def get_owner(self,obj):
        return ProfileSerializer1(obj.user.profile,many=False,read_only=True).data
