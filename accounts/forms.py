from django import forms
from allauth.account.forms import SignupForm

class SignupUserForm(SignupForm):
    name = forms.CharField(max_length=30, label='名前')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.save()
        return user

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False, )