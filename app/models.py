from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# 予約サイト
class Salon(models.Model):
    name = models.CharField('店舗', max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='店舗外観', null=True, blank=True)

    def __str__(self):
        return self.name

class Stylist(models.Model):
    stylist = models.OneToOneField(, verbose_name='スタイリスト', on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, verbose_name='店舗', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.salon}：{self.user}'

class Booking(models.Model):
    stylist = models.ForeignKey(Stylist, verbose_name='スタイリスト', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50, null=True, blank=True)
    furigana = models.CharField('フリガナ', max_length=50, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=30, null=True, blank=True)
    remarks = models.TextField('備考', default="ご要望などをお書きください", blank=True)
    start = models.DateTimeField('開始時間', default=timezone.now)
    end = models.DateTimeField('終了時間', default=timezone.now)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')
        return f'{self.name} {start} ~ {end} {self.stylist}'


# News
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

# Style一覧
class StyleCategory(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name

class Style(models.Model):
    category = models.ForeignKey(StyleCategory, verbose_name='スタイルカテゴリ', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    stylist = models.ForeignKey(Stylist, verbose_name='スタイリスト', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(MenuCategory, verbose_name='メニュカテゴリー', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class User(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    address = models.CharField('住所', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.account_core.first_name

class Staff(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.account_core.first_name