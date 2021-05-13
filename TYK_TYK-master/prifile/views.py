from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages


def profile(request, id):
    current_user = User.objects.filter(id=id).values('username', 'first_name', 'last_name', 'email', 'profile')
    user = None
    for u in current_user:
        user = u
    return render(request, 'profile.html', {'id': id, 'user': user, })