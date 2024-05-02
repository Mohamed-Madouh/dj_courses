# Generated by Django 4.2 on 2024-05-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphonenumber',
            name='type',
            field=models.CharField(choices=[('Office', 'Office'), ('Academy', 'Academy'), ('Home', 'Home'), ('Other', 'Other')], max_length=10, verbose_name='Type your number'),
        ),
    ]
