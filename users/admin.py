"""User admin classes."""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile, User
from posts.models import Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('user', 'picture')
    list_editable = ('website', 'phone_number')
    search_fields = (
        'user__email',
        'user__first_name'
    )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),

            )
        }),
    )
    readonly_fields = ('created', 'modified')


class ProfileInLine(admin.StackedInline):
    """Profile inline admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
