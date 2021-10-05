from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('api/profiles/<str:username>/', Profile.as_view()),
    path('api/board/<str:slug>/', Board.as_view()),
    path('api/create_board/', CreateBoard.as_view()),
    path('api/post/<str:slug>/', Post.as_view()),
    path('api/create_post/', CreatePost.as_view()),
    path('api/comment/<str:uid>/', Comment.as_view()),
    path('api/create_comment/', CreateComment.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)