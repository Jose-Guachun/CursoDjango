# Generated by Django 3.0.5 on 2020-05-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Admin',
            field=models.BooleanField(default=False),
        ),
    ]
