from django.contrib import admin
from apps.blog.models import Category, Comments, Blog, BlagAdmin

admin.site.register(Category)
admin.site.register(Blog, BlagAdmin)
admin.site.register(Comments)