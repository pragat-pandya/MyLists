from contextlib import redirect_stderr
from hashlib import new
from xml.dom import UserDataHandler
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .models import List, ListItem
from django.db.models import Q 

# Create your views here.
def lists (request):
  return render (request, 'list/choices.html')

@login_required(login_url='login')
def my_lists (request):
  user = Account.objects.get(username=request.user.username)
  lists  = List.objects.all().filter(Q(owner=user) | Q(contributors=user))
  return render (request, 'list/my_lists.html', {
    'lists' : lists,
    'user' : user
  })


@login_required(login_url='login')
def list_view (request, list_name):
  user = Account.objects.get (username=request.user.username)
  list = List.objects.get (list_name=list_name)
  list_items = ListItem.objects.all().filter(added_to=list)

  if request.method == 'POST':
    if 'action' in request.POST:
      action = request.POST['action']
      item = ListItem.objects.get(title=request.POST['title'])
      if action == 'done':
        item.is_done = True
        item.setted_done_by = user.username
        item.save()
        return redirect('theList', list_name=list_name)
      elif action == 'undo':
        item.is_done = False
        item.save()
        return redirect ('theList', list_name=list_name)
    if 'task' in request.POST:
      new_item = ListItem(
        title = request.POST['task'],
        added_to = list,
        contributor = user
      )
      new_item.save()
      return redirect ('theList', list_name=list_name)
      #return render (request, 'list/list.html', {
       # 'list' : List.objects.get(list_name=list_name),
        #'user' : Account.objects.get(username=request.user.username),
        #'list_items' : ListItem.objects.all().filter(added_to=list)
      #})

  return render (request, 'list/list.html', {
    'list' : list,
    'user' : user,
    'list_items' : list_items
  })