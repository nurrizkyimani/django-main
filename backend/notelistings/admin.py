from django.contrib import admin
from .models import Note

# Register your models here.

class NoteList(admin.ModelAdmin):
  list_display = ('id','title', 'instructor', 'semester', 'course', 'year')
  list_display_links = ( 'id','title')
  list_filter = ('semester', 'year')
  list_editable = ('is_published')
  search_fields = ('title', 'description', 'semester', 'course', 'instructor')
  list_per_page = 30
  
admin.site.register(Note, NoteList)