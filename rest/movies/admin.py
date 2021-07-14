from django.contrib import admin

from movies.models import Watchlist, Platform, Review


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'score')


admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Platform)
admin.site.register(Review)
