# Generated by Django 3.0.3 on 2020-05-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20200514_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='router',
            name='semester',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='router',
            name='subject',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
