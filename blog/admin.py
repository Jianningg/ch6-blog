# blog/admin.py
from django.contrib import admin
from .models import Author, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )

class PostAdmin(admin.ModelAdmin): # new
    list_display = (
        "title",
        "author",
        "body",
    )
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin) # new