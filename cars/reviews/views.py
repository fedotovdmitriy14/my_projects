from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'reviews/detailed_view.html'
    context_object_name = 'review'


class ReviewsUpdateView(UpdateView):
    model = Reviews
    template_name = 'reviews/new_review.html'

    form_class = ReviewsForm

class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = '/reviews/'
    template_name = 'reviews/review_delete.html'


def create(request):
    error = ""
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            error = 'Ошибка. Проверьте, правильно ли заполнены поля'

    form = ReviewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'reviews/new_review.html', data)


def show_reviews(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})
