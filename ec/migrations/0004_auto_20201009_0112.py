# Generated by Django 2.2.16 on 2020-10-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='purchaser_adress',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='purchaser_furigana',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='purchaser_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='purchaser_tel',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
