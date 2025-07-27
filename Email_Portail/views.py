from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import EmailForm
from .models import MessageLog, SubjectTemplate
import os
from ipware import get_client_ip

class HomeView(TemplateView):
    template_name = 'Email_Portail/home.html'

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepare email
            subject = form.cleaned_data['subject']
            recipient = form.cleaned_data['recipient']
            cc = form.cleaned_data['cc']
            bcc = form.cleaned_data['bcc']
            attachment = request.FILES.get('attachment')
            client_ip, _ = get_client_ip(request)
            
            # Format message to include sender info
            original_message = form.cleaned_data['message']
            formatted_message = f"""
            {original_message}
            
            ---
            Sent by: {form.cleaned_data['sender_email']}
            Via: College Email Portal
            """
            
            email = EmailMessage(
                subject=subject,
                body=formatted_message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Still sends from your app email
                to=[recipient.email],
                cc=[e.strip() for e in cc.split(',')] if cc else [],
                bcc=[e.strip() for e in bcc.split(',')] if bcc else [],
                reply_to=[form.cleaned_data['sender_email']]  # Replies go to student
            )
            
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            
            # Send email
            try:
                email.send()
                
                # Log the message
                MessageLog.objects.create(
                    subject=subject,
                    message=original_message,
                    recipient_email=recipient.email,
                    cc_emails=cc,
                    bcc_emails=bcc,
                    attachment_name=attachment.name if attachment else None,
                    sender_ip=client_ip,
                    sender_email=form.cleaned_data['sender_email']  # Store student email
                )
                
                messages.success(request, 'Your email has been sent successfully!')
                return redirect('success')
            except Exception as e:
                messages.error(request, f'An error occurred while sending the email: {str(e)}')
    else:
        form = EmailForm()
    
    return render(request, 'Email_Portail/send_email.html', {'form': form})

def success_view(request):
    return render(request, 'Email_Portail/success.html')

def get_template(request, template_id):
    try:
        template = SubjectTemplate.objects.get(id=template_id)
        return JsonResponse({
            'title': template.title,
            'template': template.template
        })
    except SubjectTemplate.DoesNotExist:
        return JsonResponse({'error': 'Template not found'}, status=404)