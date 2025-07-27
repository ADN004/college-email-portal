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
    list_display = ('subject', 'sender_email', 'recipient_email', 'sent_at')  # Added sender_email
    list_filter = ('sent_at', 'sender_email')  # Added filter for sender_email
    search_fields = ('subject', 'recipient_email', 'sender_email', 'message')  # Added sender_email to search
    readonly_fields = ('sent_at', 'sender_email', 'subject', 'message', 'recipient_email', 
                      'cc_emails', 'bcc_emails', 'attachment_name', 'sender_ip')  # Made all fields read-only
    date_hierarchy = 'sent_at'
    fieldsets = (
        ('Email Details', {
            'fields': ('subject', 'message', 'sender_email')
        }),
        ('Recipient Info', {
            'fields': ('recipient_email', 'cc_emails', 'bcc_emails')
        }),
        ('Metadata', {
            'fields': ('sent_at', 'sender_ip', 'attachment_name')
        }),
    )
    
    def has_add_permission(self, request):
        return False  # Prevents manual creation of logs
    
    def has_delete_permission(self, request, obj=None):
        return False  # Prevents deletion of logs (optional)