# Generated by Django 4.2 on 2024-05-03 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_image', verbose_name='userimage'),
        ),
        migrations.AddField(
            model_name='course_content',
            name='subtitell',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='doc'),
        ),
        migrations.AlterField(
            model_name='course_content',
            name='subtitel',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='about'),
        ),
    ]
