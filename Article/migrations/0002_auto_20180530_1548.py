# Generated by Django 2.0.5 on 2018-05-30 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='username',
            new_name='nickname',
        ),
    ]