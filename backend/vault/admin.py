from django.contrib import admin
from .models import APIPending
from vault.models import (
   APIPending,
   Category,
   API
)


def approve_api(modeladmin, request, queryset):
    for obj in queryset:
        API.objects.create(
            name=obj.name,
            auth=obj.auth,
            category=obj.category,
            cors=obj.cors,
            description=obj.description,
            https=obj.https,
            url=obj.url,
            owner=obj.owner
        )
        obj.delete()

approve_api.short_description = "Approve selected APIs"


class APIPendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cors', 'description', 'https', 'url')
    search_fields = ['name', 'description']

    actions = [approve_api]


class APIAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'likes_count')
    search_fields = ['name', 'description']



admin.site.register(APIPending, APIPendingAdmin)
admin.site.register(API, APIAdmin)
admin.site.register(Category)