# Generated by Django 2.1.3 on 2018-12-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('view_time', models.PositiveIntegerField(default=0)),
                ('excerpt', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
