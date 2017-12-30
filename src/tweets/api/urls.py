from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView
    )

app_name = 'tweet-api'


urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),
]
