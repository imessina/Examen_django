from django.contrib import admin
from .models import Post
from .models import Articulo
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Articulo)