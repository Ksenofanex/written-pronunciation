from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Word


class WordListView(ListView):
    model = Word
    template_name = 'dictionary/home.html'
    context_object_name = 'word_list'
    ordering = ['english'] # Ordering alphabetically.


class WordDetailView(DetailView):
    model = Word
    template_name = 'dictionary/word_detail.html'
    context_object_name = 'word'


class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    template_name = 'dictionary/word_create.html'
    fields = ('english', 'turkish',)
    login_url = 'login' # For redirecting when user isn't logged in.

    def form_valid(self, form): # For appointing the logged in user as author.
        form.instance.author = self.request.user
        return super().form_valid(form)


class WordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Word
    template_name = 'dictionary/word_update.html'
    fields = ('english', 'turkish',)

    def test_func(self): # For authorization. If logged in user is not the author itself, it can't edit & delete.
        object = self.get_object()
        return object.author == self.request.user


class WordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Word
    template_name = 'dictionary/word_delete.html'
    success_url = reverse_lazy('home') # After action is successfull, redirect to the desired page.

    def test_func(self): # For authorization. If logged in user is not the author itself, it can't edit & delete.
        object = self.get_object()
        return object.author == self.request.user


class SearchResultsView(ListView):
    model = Word
    template_name = 'dictionary/search.html'
    context_object_name = 'word_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Word.objects.filter(english__icontains=query) # Searching for field. In this case, English field.
        return object_list