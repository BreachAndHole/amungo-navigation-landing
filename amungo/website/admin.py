from django.contrib import admin

from .models import Board, BoardPhoto, VisitorMessage


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_usd', 'is_in_stock', 'lead_time_weeks')
    list_editable = ('price_usd', 'is_in_stock')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BoardPhoto)
class BoardPhotoAdmin(admin.ModelAdmin):
    list_display = ('board', 'is_title')
    list_editable = ('is_title',)


@admin.register(VisitorMessage)
class VisitorMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date')
    sortable_by = ('id', 'date')
