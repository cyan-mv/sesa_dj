# Generated by Django 4.2.5 on 2023-10-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('categories', models.JSONField()),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='DataFramesSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_frames', models.ManyToManyField(to='myapp.dataframe')),
            ],
        ),
    ]
