# Generated by Django 4.0 on 2022-01-05 20:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_profile'),
        ('memberships', '0003_remove_usermembership_membership_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pre', 'preview'), ('pub', 'published')], default='pre', max_length=10)),
                ('type', models.CharField(choices=[('single', 'single'), ('series', 'series')], default='single', max_length=10)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('age_limit', models.CharField(choices=[('rating_system_all.svg', 'All'), ('rating_system_7.svg', '7'), ('rating_system_12.svg', '12'), ('rating_system_16.svg', '16'), ('rating_system_18.svg', '18')], default='rating_system_all.svg', max_length=24)),
                ('allowed_membership', models.ManyToManyField(to='memberships.Membership')),
                ('genres', models.ManyToManyField(to='videos.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='movies')),
                ('order', models.PositiveIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField(null=True)),
                ('to_watch', models.BooleanField(null=True)),
                ('rating', models.IntegerField(choices=[(0, '☆☆☆☆☆☆☆☆☆☆'), (1, '★☆☆☆☆☆☆☆☆☆'), (2, '★★☆☆☆☆☆☆☆☆'), (3, '★★★☆☆☆☆☆☆☆'), (4, '★★★★☆☆☆☆☆☆'), (5, '★★★★★☆☆☆☆☆'), (6, '★★★★★★☆☆☆☆'), (7, '★★★★★★★☆☆☆'), (8, '★★★★★★★★☆☆'), (9, '★★★★★★★★★☆'), (10, '★★★★★★★★★★')], default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.movie')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
