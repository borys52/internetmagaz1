# Generated by Django 3.1.7 on 2021-04-03 20:43

from django.db import migrations, models
import django.db.models.deletion
import main_internetmagaz.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_internetmagaz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('photo', models.ImageField(upload_to=main_internetmagaz.models.Kind.get_file_name)),
                ('kind_order', models.IntegerField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('des', models.CharField(max_length=150, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_internetmagaz.category')),
            ],
        ),
    ]
