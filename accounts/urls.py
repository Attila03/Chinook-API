from django.conf.urls import url
from .views import UserListView, UserDetailView, RegisterView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^users/$', UserListView.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[\w-]+)', UserDetailView.as_view(), name='user_detail'),
]