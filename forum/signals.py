from .models import Profile,User,Avatar,Comment,Notification
from django.dispatch import receiver
from django.db.models.signals import post_save



def update_user_profile(sender, instance, created, **kwargs):
    """
    Signals the Profile about User creation.
    """
    if not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)
    if not Avatar.objects.filter(profile=Profile.objects.get(user=instance)).exists():
        Avatar.objects.create(profile=Profile.objects.get(user=instance))

    instance.profile.save()

post_save.connect(update_user_profile,sender=User)


# notify regarding a comment

def notify_comment(sender,instance,created, **kwargs):
    """
    Signals when a new comment is created
    """
    print("signal received")
    if(created):
        print("new comment")
        post = instance.post
        comment = instance.reply
        
        if(comment is not None): 
            n = Notification(Target=comment.profile,Object=post,Actor=instance.profile,notif_type="replied")
            n.save()
            print(n)

            if(comment.profile==post.profile):
                return 
        
        n1 = Notification(Target=post.profile,Object=post,Actor=instance.profile,notif_type="commented")
        n1.save()
        print(n1)
        
        

post_save.connect(notify_comment,sender=Comment)