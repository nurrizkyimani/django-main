from django.contrib import admin
from .models import Skilltor

# Register your models here.

class SkilltorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Skilltor, SkilltorAdmin)


