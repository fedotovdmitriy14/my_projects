from django.urls import path

from . import views

urlpatterns = [
    path('new_review/', views.create, name='create'),
    path('', views.show_reviews, name='list_of_reviews'),
    path('<int:pk>', views.ReviewsDetailView.as_view(), name='review-detail'),
    path('<int:pk>/update', views.ReviewsUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete', views.ReviewsDeleteView.as_view(), name='review-delete'),
]