from django.forms import ModelForm
from django import forms
from .models import Form, Parcel

class LogisticForm(ModelForm):
    class Meta:
        model = Parcel
        fields = ['sender_name', 'sender_address', 'weight', 'type']
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_address': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

class ExpressForm(LogisticForm):
    pass

class CourierForm(LogisticForm):
    pass

class ContactForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content', 'rows': 3}),
        }

class ProfileForm(ModelForm):
    sender_name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Parcel
        fields = ['sender_name', 'sender_address', 'sender_number', 'receiver_name', 'receiver_number', 'receiver_address', 'weight', 'type']
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_address': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_number': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_number': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }