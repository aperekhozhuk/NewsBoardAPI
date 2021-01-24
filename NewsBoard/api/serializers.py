from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author_name",
            "user_id",
        )
        extra_kwargs = {
            "creation_date": {"read_only": True},
            "upvotes": {"read_only": True},
        }
