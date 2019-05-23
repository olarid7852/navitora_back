# Generated by Django 2.0.5 on 2019-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='car_unique_id',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='name',
            field=models.CharField(default='q', max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
