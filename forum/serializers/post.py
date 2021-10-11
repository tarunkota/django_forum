from ..models import Post
from rest_framework import serializers
from .profile import ProfileSerializer1
from .board import BoardSerializer

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer1(read_only=True,many=False)
    board = BoardSerializer(read_only=True,many=False)

    class Meta:
        model = Post
        fields = ["title","slug","profile","board","text","media","question","optionA","optionB","optionC","optionD","correctOption","solution","score","active","created","updated","efficientMode","upvotes_count","downvotes_count","comments_count","postType"]
        lookup_field = 'slug'
