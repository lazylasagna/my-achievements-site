# Generated by Django 5.1.4 on 2024-12-19 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0007_achievement_rename_title_advantage_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advantage',
        ),
    ]