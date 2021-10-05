import uuid
from django.db import models

class Badge(models.Model):
    """Badges are given to users based on their activity. Pro, admin, etc.

    Attributes:
        name(str): Name of the badge
        info(str): Why is this badge given to user? Will be shown in tooltip.
        url(str): Url of the badge icon.
    """
    name = models.CharField(max_length=64)
    info = models.TextField()
    url = models.URLField()
    uid = models.UUIDField(default = uuid.uuid4,editable = False)

    def __str__(self):
        return self.name