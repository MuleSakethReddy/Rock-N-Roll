# Generated by Django 4.1.6 on 2023-04-22 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rockIT.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500, null=True)),
                ('thumbnail', models.FileField(upload_to=rockIT.models.user_directory_path)),
                ('genre', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500, null=True)),
                ('file', models.FileField(upload_to=rockIT.models.user_directory_path_file)),
                ('publisher', models.CharField(max_length=50)),
                ('speaker', models.CharField(max_length=50)),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.FileField(upload_to=rockIT.models.user_directory_path_file)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to='rockIT.album')),
            ],
        ),
    ]
