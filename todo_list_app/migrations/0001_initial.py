# Generated by Django 4.2.3 on 2023-07-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True)),
                ('is_done', models.BooleanField()),
                ('tags', models.ManyToManyField(to='todo_list_app.tag')),
            ],
        ),
    ]
