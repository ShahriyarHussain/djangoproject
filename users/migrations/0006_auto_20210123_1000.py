# Generated by Django 3.1.5 on 2021-01-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210123_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.TextField(default='', max_length=50),
        ),
    ]
