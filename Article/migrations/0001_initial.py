# Generated by Django 2.0.5 on 2018-05-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='未命名', max_length=50)),
                ('content', models.TextField(default='文档待编辑...')),
                ('likenum', models.IntegerField(default=0)),
                ('collectnum', models.IntegerField(default=0)),
                ('username', models.CharField(default='匿名', max_length=30)),
                ('userphoto', models.ImageField(default='images/q1.png', upload_to='imgs')),
                ('photo1', models.ImageField(default='images/q1.png', upload_to='imgs')),
                ('photo2', models.ImageField(default='images/q1.png', upload_to='imgs')),
                ('photo3', models.ImageField(default='images/q1.png', upload_to='imgs')),
            ],
        ),
    ]