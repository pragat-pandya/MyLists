from django.contrib import admin
from .models import List, ListItem


class ListAdmin (admin.ModelAdmin):
  model = List
  list_display = ('list_name', 'created_at', 'owner')
  list_display_links = ('list_name', 'created_at', 'owner')


class ListItemAdmin (admin.ModelAdmin):
  model = ListItem
  list_display = ('title', 'added_to', 'contributor', 'added_at', 'is_done', 'deadline')
  list_display_links = ('title', 'added_to', 'contributor', 'added_at', 'is_done', 'deadline')

# Register your models here.
admin.site.register (List, ListAdmin)
admin.site.register (ListItem, ListItemAdmin)