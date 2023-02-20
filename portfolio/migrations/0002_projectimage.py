# Generated by Django 4.1.6 on 2023-02-20 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]
