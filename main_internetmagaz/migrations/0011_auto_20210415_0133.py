# Generated by Django 3.1.7 on 2021-04-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_internetmagaz', '0010_message_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pub_time',
            field=models.TimeField(auto_now=True),
        ),
    ]