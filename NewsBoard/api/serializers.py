from rest_framework import serializers
from .models import Post, Comment, UpVote


class PostSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source="user.id")
    upvotes = serializers.SerializerMethodField()

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
        }

    def get_upvotes(self, post):
        return UpVote.objects.filter(post=post).count()


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    post_id = serializers.ReadOnlyField(source="post.id")

    class Meta:
        model = Comment
        fields = ("id", "user_id", "post_id", "author_name", "content", "creation_date")
        extra_kwargs = {
            "creation_date": {"read_only": True},
        }
