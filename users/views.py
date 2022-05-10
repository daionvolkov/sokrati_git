from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def homePage(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан!')
            return redirect('profile')
    else:
        form = UserRegForm()

    return render(request, 'users/register.html', {'title': 'Страница регистрации', 'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid():
            update_user.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
    else:
        update_user = UserUpdateForm(instance=request.user)
    data = {
        'update_user': update_user,
    }
    return render(request, 'users/profile.html', data)