from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import Tweet
from .mixins import FormUserNeededMixin
from .forms import TweetModelForm


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweets/create/'
    #login_url = '/admin/'

class TweetListView(DetailView):
    queryset = Tweet.objects.all()


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
