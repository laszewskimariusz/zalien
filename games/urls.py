from django.conf.urls import url, patterns, include
from django.contrib import admin

from .views import GamesListView


urlpatterns = [

    url(r'^$', GamesListView.as_view()),



]
