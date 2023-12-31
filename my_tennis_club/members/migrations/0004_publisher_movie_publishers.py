# Generated by Django 4.1.7 on 2023-09-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_director_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='publishers',
            field=models.ManyToManyField(to='members.publisher'),
        ),
    ]
