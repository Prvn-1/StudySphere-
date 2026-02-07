from django.contrib import admin
from .models import Resource, Rating

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'status', 'uploaded_at')
    list_filter = ('status', 'category', 'college')
    actions = ['approve_resources', 'reject_resources']

    def approve_resources(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Selected resources have been approved.")
    approve_resources.short_description = "Approve selected resources"

    def reject_resources(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Selected resources have been rejected.")
    reject_resources.short_description = "Reject selected resources"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('resource', 'user', 'stars', 'created_at')
