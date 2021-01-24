from rest_framework_nested import routers
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = routers.SimpleRouter()
router.register(r"posts", views.PostViewSet, basename="posts")

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", views.CommentViewSet, basename="post-comments")


urlpatterns = [
    path("get_token/", obtain_auth_token, name="get_token"),
    path(
        "posts/<int:post_pk>/upvote/",
        views.PostUpVoteView.as_view(),
        name="post-upvote",
    ),
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]

if settings.DEBUG:
    settings.LOGIN_REDIRECT_URL = "/api"
    settings.LOGOUT_REDIRECT_URL = "/api"

    urlpatterns.extend(
        [
            path("auth/", include("rest_framework.urls")),
        ]
    )
