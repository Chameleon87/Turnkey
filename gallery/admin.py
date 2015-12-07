from django.db import models
from django.contrib import admin
from .forms import AlbumForm
from .models import Album, Tag, Image


class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "rating", "size", "tags_", "albums_",
        "thumbnail", "created"]
    list_filter = ["tags", "albums", "user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    form = AlbumForm

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "created"]
    list_filter = ["tags", "albums"]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
