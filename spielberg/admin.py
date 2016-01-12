from django.contrib import admin

from .models import SimpleRedirect


@admin.register(SimpleRedirect)
class SimpleRedirectAdmin(admin.ModelAdmin):
    list_display = [
        'from_url',
        'to_url',
        'date_created',
        'date_modified',
        'date_active_start',
        'date_active_end',
    ]
