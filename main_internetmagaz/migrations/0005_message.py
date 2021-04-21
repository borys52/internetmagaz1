# Generated by Django 3.1.7 on 2021-04-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_internetmagaz', '0004_adress_info_maginfo_openninghours_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_message', models.CharField(max_length=400)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
    ]