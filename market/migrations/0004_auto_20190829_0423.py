# Generated by Django 2.2.4 on 2019-08-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20190829_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='phone',
        ),
    ]
