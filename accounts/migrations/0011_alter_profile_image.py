# Generated by Django 4.2 on 2024-05-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_profile_address_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile.png', upload_to='users/', verbose_name='user image'),
        ),
    ]