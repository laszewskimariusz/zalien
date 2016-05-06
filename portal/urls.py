from django.conf.urls import url

import portal.views

urlpatterns = [

    url(r'^$', portal.views.home, name='home'),

]