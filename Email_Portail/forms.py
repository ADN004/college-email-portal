from django import forms
from .models import SubjectTemplate, Recipient
from django.core.validators import FileExtensionValidator

class EmailForm(forms.Form):
    subject = forms.CharField(
        label="Subject",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email subject'})
    )
    
    subject_template = forms.ModelChoiceField(
        label="Or select a common subject",
        queryset=SubjectTemplate.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'subject-template-select'})
    )
    
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Enter your message here...'})
    )
    
    recipient = forms.ModelChoiceField(
        label="Recipient",
        queryset=Recipient.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    cc = forms.CharField(
        label="CC (comma separated emails)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email1@example.com, email2@example.com'})
    )
    
    bcc = forms.CharField(
        label="BCC (comma separated emails)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email1@example.com, email2@example.com'})
    )
    
    attachment = forms.FileField(
        label="Attachment (PDF or Image only)",
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.jpg,.jpeg,.png'})
    )
    
    def clean_cc(self):
        cc = self.cleaned_data.get('cc', '')
        if cc:
            emails = [e.strip() for e in cc.split(',')]
            for email in emails:
                if '@' not in email or '.' not in email:
                    raise forms.ValidationError(f"'{email}' is not a valid email address")
        return cc
    
    def clean_bcc(self):
        bcc = self.cleaned_data.get('bcc', '')
        if bcc:
            emails = [e.strip() for e in bcc.split(',')]
            for email in emails:
                if '@' not in email or '.' not in email:
                    raise forms.ValidationError(f"'{email}' is not a valid email address")
        return bcc