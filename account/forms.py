from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserRegistration(forms.ModelForm):
    """
    Class for creating correct form User Registration on the page.

    """
    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        """
        Function checked for equality password and password2.

        If password are equal - return password.
        Other way will return ValidationError.

        :return: password or exception.
        """
        data = self.cleaned_data

        if data.get('password') == data.get('password2'):
            return data['password2']
        raise forms.ValidationError('Error in passwords')


class UserLogin(forms.Form):
    """
    Class for creating correct form User Login on the page.

    """
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        """
        Function checked for equality password and login with data in database.

        If all OK - return function clear.
        Other way will return ValidationError.

        :return: function clean() or exception.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Error in Login or Password')
        else:
            raise forms.ValidationError('Error in Login or Password')
        return super().clean()
