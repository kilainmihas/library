# Generated by Django 4.0.4 on 2022-07-24 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='student',
        ),
    ]
