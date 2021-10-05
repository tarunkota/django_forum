from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import UniqueSlugify
from .boards import Board

class Post(models.Model):
    """Post
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150,unique=True,null=True, blank=True)
    
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE)

    text = models.TextField(max_length=5000, blank=True, null=True)
    photo = models.URLField(blank=True,default="")
    video = models.URLField(blank=True,default="")

    upvoted_by = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    downvoted_by = models.ManyToManyField(User, related_name='downvoted_posts',blank=True)
    score = models.FloatField(default=0.0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    #efficiency
    efficientMode = models.BooleanField(default=False)
    upvotes_count = models.IntegerField(default=1)
    downvotes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if(not self.efficientMode):
            self.upvotes_count=self.upvoted_by.count()
            self.downvotes_count=self.downvoted_by.count()
            self.comments_count=self.comments.count()
            super(Post, self).save(*args, **kwargs)
        #Unique slug
        self.slug = post_slugify(f"{self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def set_score(self):
        """Calculates the rank score of a post."""
        GRAVITY = 1.2
        time_delta = timezone.now() - self.created
        post_hour_age = time_delta.total_seconds()
        post_points = self.upvotes_count - 1
        self.score = post_points / pow((post_hour_age + 2), GRAVITY)
        self.save()

    @staticmethod
    def get_posts(user=None):
        """Returns a list of posts."""
        if user:
            posts = Post.objects.filter(active=True, user=user)
        else:
            posts = Post.objects.filter(active=True)
        return posts

def post_unique_check(text, uids):
    if text in uids:
        return False
    return not Post.objects.filter(slug=text).exists()


post_slugify = UniqueSlugify(unique_check=post_unique_check,
                              to_lower=True,
                              max_length=80,
                              separator='_',
                              capitalize=False)