from django.contrib import admin
from .models import Profils

# Register your models here.
class ProfilList(admin.ModelAdmin):
  list_display = ('id','description', 'chat', 'linkedin', 'about', 'experience', 'major', 'skill', 'topics')
  list_display_links = ('id','linkedin')
  list_filter = ('major', 'skill')
  # list_editable = ['is_published']
  search_fields = ('major', 'skill', 'topics')
  list_per_page = 30
  
admin.site.register(Profils, ProfilList)