from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import UniqueSlugify
from ..utils import randomCharString

class Board(models.Model):
    """Board contains posts having a similar theme.

    Attributes:
        
    """
    title = models.CharField(max_length=100, unique=True,blank=False)
    slug = models.SlugField(max_length=100, unique=True,null=True, blank=True)
    description = models.TextField(max_length=500)

    cover = models.ImageField(upload_to='board_covers/', blank=True)
    admins = models.ManyToManyField(User, related_name='inspected_boards',blank=True)

    subscribers = models.ManyToManyField(User, related_name='subscribed_boards',blank=True)
    banned_users = models.ManyToManyField(User, related_name='forbidden_boards',blank=True)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    # for efficiency
    subscriberCount = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = board_slugify(f"{self.title}")
        super().save(*args, **kwargs)



def board_unique_check(text, uids):
    if text in uids:
        return False
    return not Board.objects.filter(slug=text).exists()


board_slugify = UniqueSlugify(unique_check=board_unique_check,
                              to_lower=True,
                              max_length=80,
                              separator='_',
                              capitalize=False)