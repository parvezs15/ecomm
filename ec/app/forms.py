from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from .models import Teacher
from .models import Customer


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True',
                                                             'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': 'True',
                                                            'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.
                                PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs=
                                                                                    {'autofocus': 'True',
                                                                                     'autocomplete': 'current-password',
                                                                                     'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
    {
        'autocomplete': 'current-password',
        'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
    {
        'autocomplete': 'current-password',
        'class': 'form-control'}))


class MyPasswordResetForm(PasswordChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    pass


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "location", "city", "mobile", "state", "zipcode"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['First_name', 'Last_name', 'Applying', 'Summary', 'Email', 'ContactNumber', 'CV', 'Photo', 'Id_upload']
        widgets = {
            'First_name': forms.TextInput(attrs={
                'class': 'form-control',  # Align with Bootstrap styling
                'placeholder': 'Enter First Name',
                'style': 'width: 60%;',  # Full-width alignment
            }),
            'Last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name',
                'style': 'width: 60%;',
            }),
            'Applying': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Position Applying For',
                'style': 'width: 60%;',
            }),
            'Summary': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
                'class': 'form-control',  # Add Bootstrap styling
                'style': 'width: 80%; height: 200px; resize: none;',  # Full width, fixed height
                'placeholder': 'Enter a detailed summary here...',
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address',
                'style': 'width: 60%;',
            }),
            'ContactNumber': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Contact Number',
                'style': 'width: 60%;',
            }),
            'CV': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'Photo': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'Id_upload': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }

from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['name', 'email', 'phone', 'biography', 'subjects', 'charges_per_hour', 'profile_picture']
