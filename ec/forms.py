from django import forms

class PurchaserForm(forms.Form):
    purchaser_name = forms.CharField(max_length=50, label='名前')
    purchaser_furigana = forms.CharField(max_length=50, label='フリガナ')    
    purchaser_adress = forms.CharField(max_length=150, label='住所')    
    purchaser_tel = forms.CharField(max_length=50, label='電話番号')    
    purchaser_email = forms.CharField(max_length=50, label='メールアドレス')