# Generated by Django 3.2.6 on 2021-08-27 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]
