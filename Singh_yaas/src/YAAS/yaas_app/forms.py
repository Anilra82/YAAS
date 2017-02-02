from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from yaas_app.models import Auction


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit= True):
            user = super(MyRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()

            return user


class UserEditForm(SetPasswordForm):
    new_email = forms.EmailField(required=False,label=("New email"))
    new_password1 = forms.CharField(required=False,label=("New password"),widget=forms.PasswordInput)
    new_password2 = forms.CharField(required=False,label=("Retype same password"),widget=forms.PasswordInput)

    def save(self, commit=True):
        changed = False

        new_password = self.cleaned_data['new_password1']
        if new_password:
            self.user.set_password(new_password)
            changed = True

        new_email = self.cleaned_data['new_email']
        if new_email:
            self.user.email = new_email
            changed = True

        if changed and commit:
            self.user.save()
        return self.user


class create_auction_form(forms.ModelForm):
    class Meta:
        model = Auction



class edit_auction_form():
    class Meta:
        model = Auction

class bid_auction_form():
    class Meta:
        model = Auction

