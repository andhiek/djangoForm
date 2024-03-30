from django.contrib import admin

# Register your models here.


from .models import PostForm


class PostAdmin(admin.ModelAdmin):

    readonly_fields = [
        'slug',
        'update',
        'publish',
    ]


admin.site.register(PostForm, PostAdmin)
