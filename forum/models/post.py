from django.db import models
from django.utils import timezone
from slugify import UniqueSlugify
from .boards import Board
from .profile import Profile

class Post(models.Model):
    """Post
    """

    QUESTION="q"
    TEXT="t"
    VIDEO="v"
    IMAGE="i"
    IMAGES="j"
    LINK="l"
    FILE="f"
    POLL="p"

    POST_TYPE_CHOICES=(
        (QUESTION,QUESTION),
        (TEXT,TEXT),
        (VIDEO,VIDEO),
        (IMAGE,IMAGE),
        (LINK,LINK),
        (FILE,FILE),
        (POLL,POLL),
        )


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150,unique=True,null=True, blank=True)
    
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE)

    text = models.TextField(max_length=5000, blank=True, null=True)
    media = models.URLField(blank=True,default="")
    question = models.TextField(max_length=5000,blank=True,null=True)
    optionA = models.TextField(max_length=400,blank=True,null=True)
    optionB = models.TextField(max_length=400,blank=True,null=True)
    optionC = models.TextField(max_length=400,blank=True,null=True)
    optionD = models.TextField(max_length=400,blank=True,null=True)
    correctOption= models.CharField(max_length=1,blank=True,null=True)
    solution = models.TextField(max_length=5000,blank=True,null=True)

    upvoted_by = models.ManyToManyField(Profile, related_name='upvoted_posts', blank=True)
    downvoted_by = models.ManyToManyField(Profile, related_name='downvoted_posts',blank=True)
    score = models.FloatField(default=0.0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    #efficiency
    efficientMode = models.BooleanField(default=False)
    upvotes_count = models.IntegerField(default=1)
    downvotes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    postType = models.CharField(max_length=1,choices=POST_TYPE_CHOICES,default=TEXT)
    



    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if(not self.efficientMode):
            self.upvotes_count=self.upvoted_by.count()
            self.downvotes_count=self.downvoted_by.count()
            self.comments_count=self.comments.count()
            super(Post, self).save(*args, **kwargs)
        #Unique slug
        if(self.slug=="" or self.slug is None):
            if(self.title!=""):
                self.slug = post_slugify(f"{self.title}")
            else:
                self.slug=post_slugify(f"{self.question}")
                
        super().save(*args, **kwargs)

    def __str__(self):
        if self.title=="":
            return self.title
        else:
            return self.question

    def set_score(self):
        """Calculates the rank score of a post."""
        GRAVITY = 1.2
        time_delta = timezone.now() - self.created
        post_hour_age = time_delta.total_seconds()
        post_points = self.upvotes_count - 1
        self.score = post_points / pow((post_hour_age + 2), GRAVITY)
        self.save()


class SavedPost(models.Model):
    """
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.profile)+" " +str(self.post)  


def post_unique_check(text, uids):
    if text in uids:
        return False
    return not Post.objects.filter(slug=text).exists()


post_slugify = UniqueSlugify(unique_check=post_unique_check,
                              to_lower=True,
                              max_length=80,
                              separator='_',
                              capitalize=False)