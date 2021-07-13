from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.cache import cache
from django.core.checks import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from movie_reviews.forms import MovieForm, RegisterUserForm, LoginUserForm
from movie_reviews.models import Movie, MovieName
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView


def main_page(request):
    movies = MovieName.objects.all()
    return render(request, 'movie_reviews/base.html', {'films': movies, 'title': 'Главная страница'})

def show_movie(request, slug):
    movies = cache.get('movies')                        #API низкого уровня
    if not movies:
        movies = MovieName.objects.all()
        cache.set('movies', movies, 60)
    movie_info = MovieName.objects.filter(slug=slug)
    id = movie_info.values_list('pk')                       # получить id из queryset

    list_of_reviews = Movie.objects.filter(film_name=id[0][0])      # первый элемент кортежа из списка
    paginator = Paginator(list_of_reviews, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movie_reviews/movie_list.html', {'movies': movie_info, 'films': movies,
                                                             'title': movie_info.values_list('film_name')[0][0],
                                                             'page_obj': page_obj})

class AddReview(APIView):
    login_required = True
    def get(self, request, slug):

        form = MovieForm()
        movie = MovieName.objects.filter(slug=slug)
        return render(request, 'movie_reviews/new_review.html', {'form': form, 'form.film_name': movie})

    def post(self, request, slug):
        form = MovieForm(request.POST)
        error = ''
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('base', permanent=True)
        else:
            error = 'Ошибка. Проверьте, правильно ли заполнены поля'

        form = MovieForm()

        data = {
            'form': form,
            'error': error
        }
        return render(request, 'movie_reviews/new_review.html', data)


class ReviewsView(APIView):
    def get(self, request):
        form = MovieForm()
        return render(request, 'movie_reviews/new_review.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        error = ''
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('base', permanent=True)
        else:
            error = 'Ошибка. Проверьте, правильно ли заполнены поля'

        form = MovieForm()

        data = {
            'form': form,
            'error': error
        }
        return render(request, 'movie_reviews/new_review.html', data)


def review_list(request):
    list_of_reviews = Movie.objects.all()
    paginator = Paginator(list_of_reviews, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    reviews = Movie.objects.all()
    return render(request, "movie_reviews/review_list.html", {'page_obj': page_obj, 'movies': reviews})

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie_reviews/new_review.html'

    form_class = MovieForm

class MovieDetailView(DetailView):
    login_required = True
    model = Movie
    template_name = 'movie_reviews/detail_view.html'
    slug = "slug"
    context_object_name = 'movie'                                   #на что будем ссылаться внутри шаблона

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/reviews/'
    template_name = 'movie_reviews/delete_review.html'


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'movie_reviews/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('base')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'movie_reviews/login.html'

    def get_success_url(self):
        return reverse_lazy('base')


def logout_user(request):
    logout(request)
    return redirect('base')

