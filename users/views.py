from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm

class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    redirect_url = reverse_lazy('home')
    template_name = 'users/register.html'