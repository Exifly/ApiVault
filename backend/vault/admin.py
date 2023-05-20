from django.contrib import admin
from vault.models import (
   Category,
   API
)

class APIAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'category', 'num_likes')

admin.site.register(API, APIAdmin)
admin.site.register(Category)