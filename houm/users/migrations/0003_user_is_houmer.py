# Generated by Django 3.2.11 on 2022-02-02 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220202_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_houmer',
            field=models.BooleanField(default=False),
        ),
    ]
