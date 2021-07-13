from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Movie, MovieName


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')

class MovieNameAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'film_description')
    list_display_links = ('film_name', 'film_description')
    search_fields = ('film_name',)
    prepopulated_fields = {'slug': ('film_name',)}

    # def get_html_photo(self, object):
    #     if object.photo:
    #         return mark_safe(f'<img src = "{object.photo}, width=50>')

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieName, MovieNameAdmin)