from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    TweetCreateAPIView,
    TweetListAPIView,
    RetweetAPIView,
    )

app_name = 'tweet-api'


urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
]
