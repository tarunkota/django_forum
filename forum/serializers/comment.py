from ..models import Comment
from rest_framework import serializers
from .profile import ProfileSerializer1

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.SerializerMethodField()
    replies = RecursiveField(many=True)
    class Meta:
        model = Comment
        fields = ("uid","commented_by","text","active","score","created","updated","efficientMode","upvotes_count","downvotes_count","comments_count","replies")
        lookup_field = 'uid'

    def get_commented_by(self,obj):
        return ProfileSerializer1(obj.user.profile,many=False,read_only=True).data
