from django.shortcuts import render

def index (request):
  return render (request, 'index.html')

def forgotPassword (request):
  return render (request, 'forgotPassword.html')

def tutorial (request):
  return render (request, 'tutorial.html')