from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    furigana = forms.CharField(max_length=30, label='フリガナ')
    tel = forms.CharField(max_length=30, label='電話番号')
    remarks = forms.CharField(label='備考', widget=forms.Textarea())