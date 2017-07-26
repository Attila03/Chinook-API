from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import HomeView, RefreshTokenView
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api-token-auth/', views.obtain_auth_token, name='obtain_token'),
    url(r'^api-token-refresh/', RefreshTokenView.as_view(), name='refresh_token'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include('chinook.urls', namespace='chinook_api')),
]

