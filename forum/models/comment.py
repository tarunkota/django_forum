from django.db import models
from django.utils import timezone
from slugify import UniqueSlugify
from .post import Post
from django.db.models import Sum
import uuid
from .profile import Profile

class Comment(models.Model):
    """A comment over a post or reply to a comment.

    Args:
        models ([type]): [description]
    """
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment',related_name='replies',on_delete=models.CASCADE,null=True,blank=True)    

    uid = models.UUIDField(default = uuid.uuid4, editable = False,unique=True)
    profile = models.ForeignKey(Profile,related_name='comments',on_delete=models.CASCADE)
    text = models.TextField(blank=True,max_length=500)
    upvoted_by = models.ManyToManyField(Profile, related_name='upvoted_comments', blank=True)
    downvoted_by = models.ManyToManyField(Profile, related_name='downvoted_comments',blank=True)
    
    active = models.BooleanField(default=True)
    score = models.FloatField(default=0.0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Efficiency
    efficientMode = models.BooleanField(default=False)
    upvotes_count = models.IntegerField(default=1)
    downvotes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        if(not self.efficientMode):
            self.upvotes_count=self.upvoted_by.count()
            self.downvotes_count=self.downvoted_by.count()
            n = self.replies.aggregate(Sum('comments_count'))['comments_count__sum']
            if(n!=None):
                self.comments_count=self.replies.count() + n
            super(Comment, self).save(*args, **kwargs)
            #update parent comment
            if(self.reply!=None):
                self.reply.save()
            #update post
            if(self.post!=None):
                if(not self.post.efficientMode):
                    self.post.save()

    def __str__(self):
        return self.text

    def set_score(self):
        """Calculates the rank score of a comment."""
        GRAVITY = 1.2
        time_delta = timezone.now() - self.created
        post_hour_age = time_delta.total_seconds()
        post_points = self.upvotes_count - 1
        self.score = post_points / pow((post_hour_age + 2), GRAVITY)
        self.save()

