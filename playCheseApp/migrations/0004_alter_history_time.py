# Generated by Django 3.2.11 on 2022-02-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playCheseApp', '0003_auto_20220228_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
