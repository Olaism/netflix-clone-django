from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm

User = get_user_model()

class UserRegistrationView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'

class ProfileView(UpdateView):
    model = User
    fields = ('first_name', 'last_name')
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user