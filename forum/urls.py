from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('api/myprofile/saveAvatar/', saveAvatar,name="saveAvatar"),
    path('api/myprofile/', getMyProfile,name="getMyProfile"),

    path('api/profiles/<str:username>/', ProfileView.as_view()),
    path('api/board/<str:slug>/', BoardView.as_view()),
    path('api/create_board/', CreateBoard.as_view()),
    path('api/post/<str:slug>/', PostView.as_view()),
    path('api/create_post/',createPost,name="createPost"),
    path('api/comment/<str:uid>/', CommentView.as_view()),
    path('api/create_comment/',createComment,name="createComment" ),
    path('api/avatars/<str:profile__username>/', Avatar.as_view()),

    path('api/feed',feed,name="feed"),
    path('api/reloadfeed',feedReload,name="feedReload"),
    path('api/comments/<str:slug>/',postComments,name="comments"),
    path('api/upvote/comment/<str:uid>/', upvoteComment,name="upvoteComment"),
    path('api/upvote/post/<str:slug>/', upvotePost,name="upvotePost"),
    path('api/downvote/comment/<str:uid>/', downvoteComment,name="downvoteComment"),
    path('api/downvote/post/<str:slug>/', downvotePost,name="downvotePost"),
    path('api/votebox/post/<str:slug>/', voteboxPost,name="voteboxPost"),
    path('api/votebox/comment/<str:uid>/', voteboxComment,name="voteboxComment"),
    path('api/save/post/<str:slug>/', savePost,name="savePost"),
    path('api/joinBoard/<str:slug>/', joinBoard,name="joinBoard"),
    path('api/subscribedBoards/', getSubscribedBoards,name="getSubscribedBoards"),
    path('api/exploreBoards/', exploreBoards,name="exploreBoards"),
    path('api/<str:username>/posts/',userPosts,name="userPosts"),
    path('api/vote/poll/<str:slug>/', votePoll,name="votePoll"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)