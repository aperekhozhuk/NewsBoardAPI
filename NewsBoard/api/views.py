from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment, UpVote
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_pk")
        try:
            return Comment.objects.filter(post_id=post_id)
        except Comment.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs.get("post_pk"))


class PostUpVoteView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    # Lol, 'post' means http method here, not Post model
    def post(self, request, post_pk):
        try:
            post = Post.objects.get(id=post_pk)
        except Post.DoesNotExist:
            raise Http404
        user = request.user
        try:
            UpVote.objects.create(user=user, post=post)
            return Response({"message": "Post upvoted!"}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                {"message": "You've voted before!"}, status=status.HTTP_403_FORBIDDEN
            )
