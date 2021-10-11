from ..models import Comment
from rest_framework import serializers
from .profile import ProfileSerializer1

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveField(many=True)
    profile = ProfileSerializer1(read_only=True,many=False)

    class Meta:
        model = Comment
        fields = ("uid","profile","text","active","score","created","updated","efficientMode","upvotes_count","downvotes_count","comments_count","replies")
        lookup_field = 'uid'

    