# Generated by Django 4.1.7 on 2023-09-12 15:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_publisher_movie_publishers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='members.author')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='publishers',
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher_name',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='name',
        ),
        migrations.AddField(
            model_name='publisher',
            name='firstname',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='publisher',
            name='joindate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publisher',
            name='lastname',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='publisher',
            name='popularity_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='publisher',
            name='recommendedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.publisher'),
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='members.publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(related_name='followed_authors', to='members.user'),
        ),
        migrations.AddField(
            model_name='author',
            name='recommendedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_authors', to='members.author'),
        ),
    ]