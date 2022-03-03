# Generated by Django 3.2.11 on 2022-02-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playCheseApp', '0002_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.DateField(auto_now=True)),
                ('size', models.SmallIntegerField()),
                ('stepCnt', models.SmallIntegerField()),
                ('list', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Chese',
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.SmallIntegerField(),
        ),
    ]
