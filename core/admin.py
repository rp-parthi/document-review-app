from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Document, Comment

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role', )}),
    )

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'assigned_to', 'status', 'date_uploaded')
    list_editable = ('status',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'document', 'comment_date')