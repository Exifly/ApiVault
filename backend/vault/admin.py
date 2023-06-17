from django.contrib import admin
from vault.models import (
   Category,
   API
)

class APIAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'category', 'likes_count')

admin.site.register(API, APIAdmin)
admin.site.register(Category)