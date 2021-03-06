# Generated by Django 3.1.4 on 2020-12-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201203_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../static/img/bg.jpg', upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]
