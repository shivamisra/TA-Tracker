# Generated by Django 4.0.8 on 2023-01-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_api', '0002_auto_20230109_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmaster',
            old_name='label',
            new_name='name',
        ),
        migrations.AddField(
            model_name='groupmaster',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
