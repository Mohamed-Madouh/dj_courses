# Generated by Django 4.2 on 2024-05-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_content_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_content',
            name='urlcourses',
            field=models.URLField(null=True),
        ),
    ]
