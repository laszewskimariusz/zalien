from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import portal.views



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', portal.views.home, name='home'),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^music/', include('music.urls')),
]
