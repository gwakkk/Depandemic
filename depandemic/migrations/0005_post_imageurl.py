# Generated by Django 3.1 on 2020-10-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depandemic', '0004_auto_20200908_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageurl',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
