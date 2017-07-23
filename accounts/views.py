from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import UserSerializer
from .forms import RegistrationForm


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        print("Kwargs", kwargs)
        user = User.objects.get(pk=kwargs['pk'])
        serialized = UserSerializer(user)
        return Response(serialized.data)


class HomeView(View):

    def get(self, request, *args, **kwargs):
        print(request)
        print(request.session)
        return render(request, 'accounts/home.html')


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/Register.html', context={'form': RegistrationForm()})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            password = form.cleaned_data['password']
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            return redirect('/')
        return render(request, 'accounts/Register.html', context={'form': form})




