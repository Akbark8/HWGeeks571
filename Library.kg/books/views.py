from django.views.generic import DetailView, ListView
from .models import Book
from .forms import ReviewForm
from django.shortcuts import redirect


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = ReviewForm()
    context['reviews'] = self.object.reviews.all().order_by('-created_at')
    # Доп: средняя оценка
    reviews = self.object.reviews.all()
    if reviews.exists():
        context['avg_rating'] = round(sum(r.rating for r in reviews) / len(reviews), 1)
    else:
        context['avg_rating'] = 'Нет оценок'
    return context


def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = self.object
        review.save()
        return redirect('book_detail', pk=self.object.pk)
    return self.get(request, *args, **kwargs)


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
