# Generated by Django 3.2.6 on 2021-08-19 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210819_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]