from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.view import hello
from mysite.date import current_datetime
from mysite.time import current_datetime
from mysite.display import display
from mysite.books import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^date/$',current_datetime),
    url(r'^time/$',current_datetime),
    url(r'^display/$',display),
    #url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
)
