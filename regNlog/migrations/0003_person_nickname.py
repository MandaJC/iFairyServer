# Generated by Django 2.0.5 on 2018-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regNlog', '0002_person_userphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nickname',
            field=models.CharField(default='匿名用户', max_length=30),
        ),
    ]