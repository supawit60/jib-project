from django.contrib import admin

# Register your models here.

from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'is_available',
        'primary_phone',
        'secondary_phone',
        'address',
    )
    list_filter = (
        'is_available',
    )
