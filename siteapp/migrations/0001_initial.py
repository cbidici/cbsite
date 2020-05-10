from django.core.management import call_command
from django.db import migrations, models


def forwards(apps, schema_editor):
    Site = apps.get_model('siteapp','Site')
    site = Site(
        name='Default Site',
        sub_domain='www',
        title='Default Site',
        description='Default Site'
    )
    site.save()

def reverse(apps, schema_editor):
    print("No need to reverse data initialization for Site")


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=64)),
                ('sub_domain', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RunPython(forwards, reverse, elidable=False)
    ]
