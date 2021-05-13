from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages


def profile(request, id):
    current_user = User.objects.filter(id=id).values('username', 'first_name', 'last_name', 'email', 'profile')
    user = None
    for u in current_user:
        user = u
    pp= Profile.objects.filter(id=2).values('image')
    profile = None
    for p in pp:
        profile = p
    return render(request, 'profile.html', {'id': id, 'user': user, 'profile': profile })

def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        # messages.success(request, 'Пользователь добавлен в систему.')
        # return render(request, 'accounts/register_done.html',
        #               {'new_user': new_user})
        return redirect('/login/')
    return render(request, 'accounts/register.html', {'form': form})