from rest_framework import generics, status
from rest_framework.response import Response

from .models import Post,Comment, Follow
from .serializers import PostSerializer,CommentSerializer, FollowSerializer


class APIPosts(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-pub_date').all()
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class APIPostComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, pk):
        comments = Comment.objects.filter(post__id=pk).order_by('-created').all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            data = {
                'post': pk,
                'text': request.data['text'],
            }
        except KeyError:
            return Response({"text": "Обязательное поле"})
        serializer = CommentSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostCommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get(self, request, pk, comment_id):
        comments = Comment.objects.filter(post__id=pk).order_by('-created').all()
        try:
            serializer = CommentSerializer(comments[comment_id - 1], many=False)
            return Response(serializer.data)
        except (IndexError, ValueError):
            return Response({'msg': 'Нет записи'})

    def delete(self, request, pk, comment_id):
        try:
            comment = Comment.objects.filter(post__id=pk).order_by('-created').all()[comment_id-1]
            if comment.author == request.user:
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"msg": "нет прав доступа к записи"})
        except (IndexError, ValueError):
            return Response({'msg': 'Нет записи'})

    def put(self, request, pk, comment_id):
        try:
            comment = Comment.objects.filter(post__id=pk).order_by('-created').all()[comment_id-1]
            if comment.author == request.user:
                data = {
                    'post': pk,
                    'text': request.data['text'],
                }
                serializer = CommentSerializer(comment, data=data, many=False)
                if serializer.is_valid():
                    serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"msg":"нет прав доступа к записи"})
        except (IndexError, ValueError):
            return Response({'msg': 'Нет записи'})

    def patch(self, request, pk, comment_id):
        try:
            comment = Comment.objects.filter(post__id=pk).order_by('-created').all()[comment_id-1]
            if comment.author == request.user:
                data = {
                    'post': pk,
                    'text': request.data['text'],
                }
                serializer = CommentSerializer(comment, data=data, many=False)
                if serializer.is_valid():
                    serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"msg":"нет прав доступа к записи"})
        except (IndexError, ValueError):
            return Response({'msg': 'Нет записи'})

