# Generated by Django 4.1.6 on 2023-03-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='test_url',
            field=models.URLField(blank=True),
        ),
    ]
