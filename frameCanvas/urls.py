from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frameCanvas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# ... the rest of your URLconf goes here ...
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


