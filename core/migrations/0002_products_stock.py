# Generated by Django 4.1 on 2023-02-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
