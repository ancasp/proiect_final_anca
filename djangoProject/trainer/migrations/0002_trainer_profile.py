# Generated by Django 4.2.7 on 2023-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(null=True, upload_to='profile_trainers/'),
        ),
    ]