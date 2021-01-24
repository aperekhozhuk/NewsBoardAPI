from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter()
router.register(r"posts", views.PostViewSet)


urlpatterns = [
    path("get_token/", obtain_auth_token, name="get_token"),
    path("", include(router.urls)),
]

if settings.DEBUG == True:
    settings.LOGIN_REDIRECT_URL = "/api"
    settings.LOGOUT_REDIRECT_URL = "/api"

    urlpatterns.extend(
        [
            path("auth/", include("rest_framework.urls")),
        ]
    )
