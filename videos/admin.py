from django.contrib import admin

from videos.models import Genre, Movie, Video, UserMovie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class VideoAdminInline(admin.TabularInline):
    model = Video
    extra = 1


class UserMovieAdminInline(admin.TabularInline):
    model = UserMovie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status', 'type', 'age_limit']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status', 'age_limit', ]
    list_filter = ['genres', 'publish', 'status', 'type', 'allowed_membership', 'age_limit']
    search_fields = ['title', 'description', ]
    inlines = [VideoAdminInline, ]
    ordering = ['status', '-publish', ]
