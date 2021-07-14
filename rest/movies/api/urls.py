from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'platforms', views.StreamPlatform, basename='platform')

urlpatterns = [
    path('movies/', views.WatchListAPI.as_view(), name='list'),
    path('movies/<int:pk>', views.WatchListObjectAPI.as_view(), name='obj'),

    path('', include(router.urls)),
    # path('platforms/', views.PlatformAPI.as_view(), name='platforms'),
    # path('platforms/<int:pk>/', views.PlatformAPIobj.as_view(), name='plobj'),


    # path('reviews/', views.ReviewList.as_view(), name='review_list'),
    # path('reviews/<int:pk>', views.ReviewDetail.as_view(), name=

    path('<int:pk>/review-create', views.ReviewCreate.as_view(), name='review_create'),
    path('movies/<int:pk>/reviews/', views.ReviewList.as_view(), name='review_list'),
    path('movies/reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

    path('user/', views.UserReviews.as_view(), name='user_review'),

    path('list/', views.Movies.as_view(), name='test_list'),
]