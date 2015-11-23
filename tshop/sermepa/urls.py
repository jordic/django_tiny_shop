from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('sermepa.views',
    url(
        regex=r'^$',
        view='sermepa_ipn',
        name='sermepa_ipn',
    ),
)
