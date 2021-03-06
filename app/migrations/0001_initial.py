# Generated by Django 2.2.16 on 2020-09-29 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='店舗')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号')),
                ('description', models.TextField(blank=True, default='', verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='店舗外観')),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Salon', verbose_name='店舗')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='スタイリスト')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='名前')),
                ('furigana', models.CharField(blank=True, max_length=50, null=True, verbose_name='フリガナ')),
                ('tel', models.CharField(blank=True, max_length=30, null=True, verbose_name='電話番号')),
                ('remarks', models.TextField(blank=True, default='ご要望などをお書きください', verbose_name='備考')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Stylist', verbose_name='スタイリスト')),
            ],
        ),
    ]
