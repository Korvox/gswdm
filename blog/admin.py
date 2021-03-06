from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
  date_hierarchy = "created_at"
  fields = ("published", "title", "content", "author", "slug")
  list_display = ["published", "title", "updated_at", "author"]
  list_display_links = ["title"]
  list_editable = ["published"]
  list_filter = ["published", "updated_at", "author"]
  prepopulated_fields = {"slug" : ("title",)}
#  readonly_fields = ("slug",)
  search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)
