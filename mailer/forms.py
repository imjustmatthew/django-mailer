import re

from django import forms
from django.core.mail import EmailMultiAlternatives
from django.contrib.admin.widgets import AdminTextInputWidget, AdminTextareaWidget

from mailer.models import Message, make_message


class MessageForm(forms.ModelForm):
    from_email = forms.CharField(widget=AdminTextInputWidget())
    to = forms.CharField(widget=AdminTextInputWidget())
    subject = forms.CharField(widget=AdminTextInputWidget())
    body = forms.CharField(widget=AdminTextareaWidget)
    body_html = forms.CharField(required=False, widget=AdminTextareaWidget)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            if not kwargs.get('initial'):
                kwargs['initial'] = {}
            kwargs['initial']['from_email'] = instance.from_address
            kwargs['initial']['to'] = instance.to_addresses
            kwargs['initial']['subject'] = instance.subject
            kwargs['initial']['body'] = instance.body
            kwargs['initial']['body_html'] = instance.body_html
        return super(MessageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance = make_message(db_msg=instance,
                                from_email=self.cleaned_data['from_email'],
                                to=re.split(", *", self.cleaned_data['to']),
                                subject=self.cleaned_data['subject'],
                                body=self.cleaned_data['body'])

        body_html = self.cleaned_data['body_html']
        if body_html:
            email = instance.email
            email = EmailMultiAlternatives(email.subject, email.body, email.from_email, email.to)
            email.attach_alternative(body_html, "text/html")
            instance.email = email

        if commit:
            instance.save()
        return instance

    class Meta:
        model = Message
        fields = ('from_email', 'to', 'subject', 'body', 'body_html', 'priority')
