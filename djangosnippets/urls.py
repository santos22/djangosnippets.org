from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('manage/', admin.site.urls),
    path('bookmarks/', include('cab.urls.bookmarks')),
    path('comments/', include('django_comments.urls')),
    path('feeds/', include('cab.urls.feeds')),
    path('languages/', include('cab.urls.languages')),
    path('popular/', include('cab.urls.popular')),
    path('search/', include('cab.urls.search')),
    path('snippets/', include('cab.urls.snippets')),
    path('tags/', include('cab.urls.tags')),
    path('users/', include('cab.urls.users')),
    path('', lambda request: render(request, 'homepage.html'), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
