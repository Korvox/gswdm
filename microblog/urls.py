from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView
from . import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Examples:
# url(r'^$', 'microblog.views.home', name='home'),
# url(r'^microblog/', include('microblog.foo.urls')),
# url(r'^$', TemplateView.as_view(template_name="index.html")),
# Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
  url(r"^$", views.HomepageView.as_view(), name="home"),
  url(r"^blog/", include("blog.urls", namespace="blog")),
)

urlpatterns += patterns('',
  (r'^static/(.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}),
)
