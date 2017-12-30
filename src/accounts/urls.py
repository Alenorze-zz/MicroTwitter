from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView
    )

app_name = 'profiles'


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
]
