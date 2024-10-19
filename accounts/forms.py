from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'contact_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username or Contact Number')

    def clean(self):
        username = self.cleaned_data.get('username')
        if username:
            try:
                # Check if the input is an email
                user = CustomUser .objects.get(email=username)
            except CustomUser .DoesNotExist:
                try:
                    # Check if the input is a username
                    user = CustomUser .objects.get(username=username)
                except CustomUser .DoesNotExist:
                    try:
                        # Check if the input is a contact number
                        user = CustomUser .objects.get(contact_number=username)
                    except CustomUser .DoesNotExist:
                        raise forms.ValidationError("Invalid username/email/contact number.")
        return self.cleaned_data
# forms.py
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    contact_number = forms.CharField(max_length=15, label="Contact Number")

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")