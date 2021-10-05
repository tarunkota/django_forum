from django.contrib import admin
from .models import *

admin.site.register(Badge)

class ProfileAdmin(admin.ModelAdmin):
    exclude=['followers','contact_list','pending_list']

admin.site.register(Profile, ProfileAdmin)


class BoardAdmin(admin.ModelAdmin):
    # exclude=['admins','subscribers','banned_users']
    pass
admin.site.register(Board, BoardAdmin)


class PostAdmin(admin.ModelAdmin):
    # exclude=['user','upvoted_by','downvoted_by',]
    pass

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    # exclude=['upvoted_by','downvoted_by','commenter','post','reply']
    pass

admin.site.register(Comment, CommentAdmin)
