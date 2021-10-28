from ..serializers import NotificationSerializer
from ..models import Notification
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotifications(request):
    notifications = Notification.objects.filter(Target=request.user.profile).order_by('is_read','-created')[0:10]
    data ={}
    data["notifications"] = NotificationSerializer(notifications,many=True).data
    data["unread"] = Notification.objects.filter(Target=request.user.profile).filter(is_read=False).count()
    return JsonResponse(data,safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def readNotification(request,id):
    n = Notification.objects.filter(Target = request.user.profile,id=id).all()
    n.update(is_read=True)
    return JsonResponse({"msg":"success"})


