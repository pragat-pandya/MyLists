from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def lists (request):
  return render (request, 'list/choices.html')

@login_required(login_url='login')
def my_lists (request):
  return render (request, 'list/my_lists.html')