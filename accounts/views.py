from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework import generics, renderers, parsers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from .forms import RegistrationForm


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(APIView):

    def get(self, request, *args, **kwargs):
        # print(request.user)
        # print("Kwargs", kwargs)
        user = User.objects.get(pk=kwargs['pk'])
        serialized = UserSerializer(user)
        return Response(serialized.data)


class RefreshTokenView(APIView):

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            prev_token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        else:
            prev_token.delete()
            token = Token.objects.create(user=user)
        return Response({'token': token.key})


class HomeView(View):

    def get(self, request, *args, **kwargs):
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


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
