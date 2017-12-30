from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView

User = get_user_model()

class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
                    User,
                    username_iexact=self.kwargs.get("username")
                    )   
