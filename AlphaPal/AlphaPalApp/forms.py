from django.forms import ModelForm
from django import forms
from .models import Client, Transaction,Account


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','email','birthday','user_image','location']
        widgets = {
            'location': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super(ClientForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

