# Generated by Django 2.0.5 on 2018-05-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regNlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='userphoto',
            field=models.ImageField(default='images/q1.png', upload_to='imgs'),
        ),
    ]
