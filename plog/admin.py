# from django.contrib import admin
# from plog.models import Blog

# from tinymce.widgets import TinyMCE
# from django.db import models

# class BlogAdmin(admin.ModelAdmin):
#     formfield_overrides={models.TextField:{'widget':TinyMCE()}}




# # Register your models here.
# admin.site.register(Blog)
from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from plog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    class Media:
        css={
            "all":("css/main.css",)
        }
        js=("js/blog.js",)

admin.site.register(Blog, BlogAdmin)
