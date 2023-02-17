from django import forms
from .models import UserReservation, ContactUs


class ContactUsForm(forms.ModelForm):
    """
    Class for creating correct form Contact Us on the page.
    
    All variables inside HTML-tags.
    """

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
        })
    )

    email = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'name': 'email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email',
        })
    )

    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'subject',
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Subject',
        })
    )

    message = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={
            'name': 'message',
            'type': 'message',
            'class': 'form-control',
            'rows': '5',
            'placeholder': 'Message',
        })
    )

    class Meta:

        model = ContactUs
        fields = ('name', 'email', 'subject', 'message')


class UserReservationForm(forms.ModelForm):
    """Class for creating correct form User Reservation on the page.
    
    All variables inside HTML-tags.
    """

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )

    email = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'name': 'email',
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email'
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'phone',
            'class': 'form-control',
            'id': 'phone',
            'placeholder': 'Your Phone',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 10 chars'
        })
    )

    date_reservation = forms.CharField(
        widget=forms.DateInput(attrs={
            'type': 'text',
            'name': 'date',
            'class': 'form-control',
            'id': 'date',
            'placeholder': 'Date',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )

    time_reservation = forms.CharField(
        widget=forms.TimeInput(attrs={
            'type': 'text',
            'name': 'time',
            'class': 'form-control',
            'id': 'time',
            'placeholder': 'Time',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )

    persons = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'name': 'people',
            'class': 'form-control',
            'id': 'people',
            'placeholder': '# of people',
            'data-rule': 'minlen:1',
            'data-msg': 'Please enter at least 1 chars'
        })
    )

    message = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={
            'name': 'message',
            'type': 'message',
            'class': 'form-control',
            'rows': '5',
            'placeholder': 'Message',
        })
    )

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'date_reservation', 'time_reservation', 'persons', 'message')
