# Generated by Django 3.0.5 on 2020-04-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chrisapp', '0003_auto_20200417_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='punchline_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]