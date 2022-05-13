from django.db import models
from accounts.models import Account


# Create your models here.

class ListItem (models.Model):
  title = models.CharField (max_length=500, unique=True)
  added_to = models.ForeignKey ('List', related_name='parent', on_delete=models.CASCADE)
  contributor = models.ForeignKey (Account, on_delete=models.CASCADE)
  added_at = models.DateTimeField (auto_now_add=True)
  is_done = models.BooleanField (default=False)
  setted_done_by = models.CharField(max_length=200, blank=True)
  deadline = models.DateTimeField (blank=True, null=True)


class List (models.Model):
  list_name = models.CharField (max_length=100)
  description = models.CharField (max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(Account, on_delete=models.CASCADE)
  contributors = models.ManyToManyField(Account, related_name='contributors')
  list_items = models.ManyToManyField(ListItem, related_name='items', blank=True)
