# Generated by Django 3.1.4 on 2020-12-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201205_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../img/default.jpg', upload_to='../img'),
        ),
    ]