# Generated by Django 5.0.1 on 2024-01-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetvigil', '0005_alter_capturedimage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capturedimage',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
