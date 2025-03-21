# Generated by Django 3.2.25 on 2025-03-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='owner',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
