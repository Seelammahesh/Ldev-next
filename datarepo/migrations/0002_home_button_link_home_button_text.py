# Generated by Django 4.2.7 on 2023-11-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='button_link',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='button_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
