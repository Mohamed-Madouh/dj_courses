# Generated by Django 4.2 on 2024-05-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_dateofbirthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphonenumber',
            name='type',
            field=models.CharField(choices=[('Academy', 'Academy'), ('Home', 'Home'), ('Other', 'Other'), ('Office', 'Office')], max_length=10, verbose_name='Type your number'),
        ),
    ]
