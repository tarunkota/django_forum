import json
from ..models import Profile,Avatar
from ..serializers import ProfileSerializer1
from rest_framework import generics
from rest_framework import permissions
from .utils import IsOwnerOrReadOnly

from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Args:
        generics ([type]): [description]
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer1
    lookup_field = 'username'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyProfile(request):
    """
    """
    profile = Profile.objects.get(user= request.user)
    data = ProfileSerializer1(profile).data
    return JsonResponse(data,safe=False)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def saveAvatar(request):
    """
    """
    avatar = Avatar.objects.get(profile__user=request.user)
    d=json.loads(request.body)
    print(d)
    data = d['avatar']
    # save
    avatar.topType = data['topType']
    avatar.accessoriesType = data['accessoriesType']
    avatar.hairColor = data['hairColor']
    avatar.facialHairType = data['facialHairType']
    avatar.facialHairColor = data['facialHairColor']
    avatar.clotheType = data['clotheType']
    avatar.clotheColor = data['clotheColor']
    avatar.graphicType = data['graphicType']
    avatar.eyeType = data['eyeType']
    avatar.eyebrowType = data['eyebrowType']
    avatar.mouthType = data['mouthType']
    avatar.skinColor = data['skinColor']
    avatar.save()

    #reload posts of this user

    return JsonResponse({"msg":"success"})