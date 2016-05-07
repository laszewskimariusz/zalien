from django.conf.urls import url

import userprofile.views

urlpatterns = [

    url(r'^$', userprofile.views.profile, name='profile'),

]