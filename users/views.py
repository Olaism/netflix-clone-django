from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model

class UserListView(ListView):
    model = get_user_model()
