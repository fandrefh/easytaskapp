from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(request, 'Usuário criado com sucesso. Utilize o formulário abaixo para fazer login.')
            return redirect('accounts:user_login')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválido.')
    return render(request, 'accounts/user_login.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Não foi possível alterar sua senha.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')
