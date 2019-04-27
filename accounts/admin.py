from django.contrib import admin

from accounts.models import User


@admin.register(User)
class SiteAdmin(admin.ModelAdmin):
    fields = (
        'is_superuser',
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'parent_id',
        'date_joined',
        'salary',
        'position'
    )
    list_display = ('username', 'first_name', 'last_name', 'position')

