# Generated by Django 3.2.18 on 2025-04-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0010_auto_20250417_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='user_image/')),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'user_list',
            },
        ),
    ]
