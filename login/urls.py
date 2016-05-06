from django.conf.urls import url

import login.views

urlpatterns = [

    url(r'^$', login.views.login, name='login'),

]