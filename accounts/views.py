from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login (request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate (username=username, password=password)
    if user is not None:
      auth.login (request, user)
      messages.success (request, f'You are now logged in as {user.username}!')
      return redirect ('homepage')
    else:
      messages.error (request, 'Invalid login credential!')
  else:
    return render (request, 'accounts/login.html')



@login_required (login_url = 'login')
def logout (request):
  auth.logout(request)
  messages.success(request, 'You are now logged out!')
  return redirect ('homepage')