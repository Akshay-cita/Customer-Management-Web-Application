# Generated by Django 3.0.3 on 2020-07-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_study_app1', '0007_auto_20200715_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/profile1.png', null=True, upload_to=''),
        ),
    ]
