from .views import main_page, ReviewsView, review_list, MovieUpdateView, MovieDetailView, MovieDeleteView, show_movie, \
    AddReview, RegisterUser, login, LoginUser, logout_user
from django.urls import path

urlpatterns = [
    path("", main_page, name='base'),
    path("new_review/", ReviewsView.as_view(), name='reviews'),
    path("reviews/", review_list, name="list"),
    path("reviews/<int:pk>", MovieDetailView.as_view(), name="details"),
    path("reviews/<int:pk>/update", MovieUpdateView.as_view(), name="update"),
    path("reviews/<int:pk>/delete", MovieDeleteView.as_view(), name="delete"),
    path("movies/<slug:slug>", show_movie, name="movie_list"),
    path("movies/<slug:slug>/add", AddReview.as_view(), name="add"),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
