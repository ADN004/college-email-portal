from django.db import models
from django.core.validators import FileExtensionValidator

class SubjectTemplate(models.Model):
    title = models.CharField(max_length=200, unique=True)
    template = models.TextField(help_text="Default message template for this subject")
    
    def __str__(self):
        return self.title

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100, help_text="E.g., Principal, Office, HOD")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.role})"

class MessageLog(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipient_email = models.EmailField()
    cc_emails = models.TextField(blank=True, null=True)
    bcc_emails = models.TextField(blank=True, null=True)
    attachment_name = models.CharField(max_length=255, blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    sender_ip = models.GenericIPAddressField(blank=True, null=True)
    
    def __str__(self):
        return f"Email to {self.recipient_email} at {self.sent_at}"