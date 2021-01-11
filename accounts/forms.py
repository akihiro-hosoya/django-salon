from django import forms
from .models import CustomUser
from app.models import User, Staff
from allauth.account.forms import SignupForm

class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=100, label='姓')
    last_name = forms.CharField(max_length=100, label='名')
    address = forms.CharField(max_length=100, label='住所')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user_profile = User()
        user_profile.account_core = CustomUser.objects.filter(email=self.cleaned_data['email'])[0]
        user_profile.first_name = self.cleaned_data['first_name']
        user_profile.last_name = self.cleaned_data['last_name']
        user_profile.address = self.cleaned_data['address']
        user_profile.save()
        return user

class SignupStaffForm(SignupForm):
    first_name = forms.CharField(max_length=100, label='姓')
    last_name = forms.CharField(max_length=100, label='名')
    tel = forms.CharField(max_length=100, label='電話番号')

    def save(self, request):
        user = super(SignupStaffForm, self).save(request)
        staff = Staff()
        staff.account_core = CustomUser.objects.filter(email=self.cleaned_data['email'])[0]
        staff.first_name = self.cleaned_data['first_name']
        staff.last_name = self.cleaned_data['last_name']
        staff.tel = self.cleaned_data['tel']
        staff.save()
        return user

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False, )