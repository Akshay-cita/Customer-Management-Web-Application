# Generated by Django 3.0.3 on 2020-07-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_study_app1', '0002_auto_20200706_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='for_study_app1.Tag'),
        ),
    ]
