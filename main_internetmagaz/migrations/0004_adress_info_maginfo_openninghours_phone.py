# Generated by Django 3.1.7 on 2021-04-04 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_internetmagaz', '0003_kind_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('building', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('maz_infp', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='')),
                ('is_visible', models.BooleanField(default=True)),
                ('des', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('hours', models.CharField(max_length=12)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MagInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_internetmagaz.adress')),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_internetmagaz.phone')),
            ],
        ),
    ]
