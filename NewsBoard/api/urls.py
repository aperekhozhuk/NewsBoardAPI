from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path("get_token/", obtain_auth_token, name="get_token"),
]
