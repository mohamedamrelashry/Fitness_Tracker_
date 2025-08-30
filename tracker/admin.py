from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('user__username', 'activity_type')
