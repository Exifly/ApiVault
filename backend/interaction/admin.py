from .models import Like, Feedback
from django.contrib import admin


class CustomFeedbacksAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "message", "user")
    search_fields = ("name",  "id")


admin.site.register(Like)
admin.site.register(Feedback, CustomFeedbacksAdmin)
