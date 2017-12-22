from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import Tweet
from .forms import TweetModelForm

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweets/create/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


class TweetListView(DetailView):
    queryset = Tweet.objects.all()


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
