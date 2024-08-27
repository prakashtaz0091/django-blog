from django.contrib import admin
from .models import Profile, Post, Tag, Comment, Likes, PostTag
from django.contrib.auth.models import User


class ProfileInline(admin.TabularInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Profile)
admin.site.register(PostTag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)