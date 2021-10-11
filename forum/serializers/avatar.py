from ..models import Avatar
from rest_framework import serializers

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ["background","topType","accessoriesType","hairColor","facialHairType","facialHairColor","clotheType","clotheColor","graphicType","eyeType","eyebrowType","mouthType","skinColor"]
    