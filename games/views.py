from django.shortcuts import render
from django.views.generic import ListView
from django.core.files import File

from .models import Games


class GamesListView(ListView):
    model = Games

from django.shortcuts import render
