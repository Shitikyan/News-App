from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Tag, Author, News, DecorativeImages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        ('General Information', {
            'fields': ('name',)
        }),

        ('Content', {
            'fields': ('cover_image',)
        }),

    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DecorativeImages)
class DecorativeImagesAdmin(admin.ModelAdmin):
    list_display = ('image',)
    fieldsets = (

        ('Content', {
            'fields': ('image',)
        }),

    )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'category', 'featured')
    search_fields = ('title', 'author__user__username', 'category__name')
    list_filter = ('category', 'tags', 'featured')

    fieldsets = (
        ('General Information', {
            'fields': ('title', 'category', 'tags', 'featured')
        }),
        ('Content', {
            'fields': ('text', 'cover_image_url')
        }),
        ('Statistics', {
            'fields': ('view_count',)
        }),
    )

    readonly_fields = ('date', 'view_count')


    def save_model(self, request, obj, form, change):
        if not obj.author_id and not change:
            obj.author = Author.objects.get_or_create(user=request.user)[0]
        super().save_model(request, obj, form, change)


class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = 'Author Information'

class CustomUserAdmin(UserAdmin):
    inlines = (AuthorInline,)


admin.site.site_header = "Solicy News Admin"
admin.site.index_title = "System Administrator Dashboard"

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)    