# Generated by Django 3.2.6 on 2021-08-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210818_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
