# Generated by Django 4.1.5 on 2023-01-25 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Default.png', null=True, upload_to='images/'),
        ),
    ]
