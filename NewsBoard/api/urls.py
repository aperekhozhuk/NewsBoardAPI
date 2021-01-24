from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = DefaultRouter()
router.register(r"posts", views.PostViewSet)


urlpatterns = [
    path("get_token/", obtain_auth_token, name="get_token"),
    path("", include(router.urls)),
]
