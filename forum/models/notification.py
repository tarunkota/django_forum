from django.contrib.auth.models import User
from django.db import models

from .post import Post
from .profile import Profile


class Notification(models.Model):
    """
    Model that represents a notification.
    """
    NOTIF_CHOICES = (

        # commented on a post by user
        ('commented',"commented on your post"),
        # replied to a comment by user
        ('replied',"replied to your comment"),
        
        # these 2 later
        # ('sent_msg_request', 'Sent a Message Request'),
        # ('confirmed_msg_request', 'Sent a Message Request'),
    )

    Actor = models.ForeignKey(Profile, related_name='c_acts', on_delete=models.CASCADE)
    Object = models.ForeignKey(Post, related_name='act_notif', null=True, blank=True, on_delete=models.SET_NULL)
    Target = models.ForeignKey(Profile, related_name='c_notif', on_delete=models.CASCADE)

    notif_type = models.CharField(max_length=500, choices=NOTIF_CHOICES, default='commented on your post')
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )


    def __str__(self):
        return str(self.Target)
