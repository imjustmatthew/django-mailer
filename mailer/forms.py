import re

from django import forms

from mailer.models import Message, make_message


class MessageForm(forms.ModelForm):
    from_email = forms.CharField()
    to = forms.CharField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            if not kwargs.get('initial'):
                kwargs['initial'] = {}
            kwargs['initial']['from_email'] = instance.from_address
            kwargs['initial']['to'] = instance.to_addresses
            kwargs['initial']['subject'] = instance.subject
            kwargs['initial']['body'] = instance.body
        return super(MessageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance = make_message(db_msg=instance,
                                from_email=self.cleaned_data['from_email'],
                                to=re.split(", *", self.cleaned_data['to']),
                                subject=self.cleaned_data['subject'],
                                body=self.cleaned_data['body'])
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Message
        fields = ('from_email', 'to', 'subject', 'body', 'when_added', 'priority')
