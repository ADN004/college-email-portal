from django.contrib import admin
from .models import SubjectTemplate, Recipient, MessageLog

@admin.register(SubjectTemplate)
class SubjectTemplateAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('name', 'email', 'role')
    list_editable = ('is_active',)
    ordering = ('role', 'name')

@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient_email', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'recipient_email', 'message')
    readonly_fields = ('sent_at',)
    date_hierarchy = 'sent_at'
    
    def has_add_permission(self, request):
        return False