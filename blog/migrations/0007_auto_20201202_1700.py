# Generated by Django 2.1.15 on 2020-12-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201202_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]
