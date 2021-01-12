from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Organization

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(label = 'Date of Birth',help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ("username", "email", "dob","password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user_profile = Profile(user=user, dob = self.cleaned_data.get('dob'))
            user_profile.save()
        return user
