from urllib import request

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, viewsets, filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework.views import APIView

from movies.api.pagination import ReviewListPagination
from movies.api.permissions import AdminOrReadOnly, ReviewUserOrReadonly
from movies.api.serializers import WatchListSerializer, PlatformSerializer, ReviewSerializer
from movies.api.throttling import ReviewListThrottle
from movies.models import Watchlist, Platform, Review

# for test:

class Movies(generics.ListAPIView):
    serializer_class = WatchListSerializer
    queryset = Watchlist.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class UserReviews(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        queryset = Review.objects.filter(review_user__username=username)
        return queryset


# without mixins:

class ReviewList(generics.ListAPIView):
    # throttle_classes = [ReviewListThrottle]
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', 'description', 'review_user__username']
    pagination_class = ReviewListPagination

    # а теперь переписываем queryset:
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # we need to override the QS cause we are passing the exact id, not all
    # по умолчанию вызывается метод perform_create, который сохраняет serializer
    def get_queryset(self):
        queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']      # либо self.kwargs.get('pk')
        movie = Watchlist.objects.get(pk=pk)

        user = self.request.user
        review_queryset = Review.objects.filter(review_user=user, watchlist=movie)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')

        if movie.num_of_ratings == 0:
            movie.average_rating = serializer.validated_data['rating']
            movie.avg_rating_previous = movie.average_rating
        else:
            movie.avg_rating_previous = movie.average_rating
            movie.average_rating = (movie.average_rating + serializer.validated_data['rating']) / 2

        movie.num_of_ratings = movie.num_of_ratings + 1
        movie.save()

        serializer.save(watchlist=movie, review_user=user)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadonly]

    def perform_destroy(self, serializer):
        # доставем id текущего review и находим это review
        pk = self.kwargs['pk']  # либо self.kwargs.get('pk')
        review = Review.objects.get(pk=pk)

        # у конкретного review выуживаем название связанного с ним фильма (из-за метода str)
        film = review.watchlist
        # ищем фильм с этим названием
        movie = Watchlist.objects.get(title=film)
        # и уменьшаем его кол-во просмотров
        movie.num_of_ratings = movie.num_of_ratings - 1
        movie.average_rating = movie.avg_rating_previous
        movie.save()

        serializer.delete()

# with mixins:

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class =ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class WatchListAPI(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchListSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListObjectAPI(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'Movie is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)  # конкретизируем
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatform(viewsets.ModelViewSet):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()
    permission_classes = [AdminOrReadOnly]


# class StreamPlatform(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Platform.objects.all()
#         serializer = PlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Platform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = PlatformSerializer(watchlist)
#         return Response(serializer.data)


#
# class PlatformAPI(APIView):
#     def get(self, request):
#         platforms = Platform.objects.all()
#         serializer = PlatformSerializer(platforms, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def put(self, request):
#         serializer = PlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# class PlatformAPIobj(APIView):
#     def get(self, request, pk):
#         try:
#             platform = Platform.objects.get(pk=pk)
#         except Platform.DoesNotExist:
#             return Response({'Error': 'Platform is not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PlatformSerializer(platform, context={'request': request})
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         platform = Platform.objects.get(pk=pk)
#         serializer = PlatformSerializer(platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         platform = Platform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
#
# def show_list(request):
#
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)         # на этом этапе связываем с моделью
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def show_movie(request, pk):
#
#     if request.method == 'GET':
#
#         try:
#             movie = Movie.objects.get(pk=pk)
#
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie is not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)                   # конкретизируем
#         serializer = MovieSerializer(movie, data=request.data)      # старые данные(movie) и новые(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)