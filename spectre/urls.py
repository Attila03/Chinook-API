from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include('chinook.urls', namespace='chinook_api')),
]

