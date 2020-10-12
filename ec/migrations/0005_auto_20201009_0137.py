# Generated by Django 2.2.16 on 2020-10-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0004_auto_20201009_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_name', models.CharField(max_length=50)),
                ('purchaser_furigana', models.CharField(max_length=50)),
                ('purchaser_adress', models.CharField(max_length=150)),
                ('purchaser_tel', models.CharField(max_length=50)),
                ('purchaser_email', models.CharField(max_length=50)),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='purchaser_adress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='purchaser_furigana',
        ),
        migrations.RemoveField(
            model_name='order',
            name='purchaser_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='purchaser_tel',
        ),
    ]