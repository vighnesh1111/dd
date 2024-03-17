# Generated by Django 4.0.6 on 2024-01-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetvigil', '0002_alter_capturedimage_options_capturedimage_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturedimage',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capturedimage',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capturedimage',
            name='rewards',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='capturedimage',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
