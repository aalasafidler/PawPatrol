from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
@login_required(login_url="/accounts/login/")
def stats_view(request):
    return render(request, 'stats/stats.html')