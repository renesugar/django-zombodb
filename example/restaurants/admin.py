from django.contrib import admin

from django_zombodb.admin_mixins import ZomboDBAdminMixin
from restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(ZomboDBAdminMixin, admin.ModelAdmin):
    model = Restaurant
    list_display = (
        'name',
        '_zombodb_score',
        'street',
        'zip_code',
        'city',
        'state',
        'phone',
        'categories',
    )

    class Media:
        js = ('django_zombodb/js/hide_show_score.js',)
